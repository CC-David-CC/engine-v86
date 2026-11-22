#!/usr/bin/env node

import assert from "node:assert/strict";
import { PS2 } from "../../src/ps2.js";

const cpu = {
    io: { register_read() {}, register_write() {} },
    device_raise_irq() {}, device_lower_irq() {},
};
const ps2 = new PS2(cpu, { register() {} });
ps2.use_mouse = ps2.enable_mouse_stream = ps2.enable_keyboard_stream = true;

function drain()
{
    const output = [];
    while(ps2.next_byte_is_ready)
    {
        const device = ps2.next_byte_is_aux ? "aux" : "kbd";
        output.push([device, ps2.port60_read()]);
    }
    return output;
}

ps2.mouse_send_click(true, false, false);
ps2.kbd_send_code(0x11);
ps2.mouse_send_click(false, false, false);
ps2.kbd_send_code(0x91);
assert.deepEqual(drain(), [
    ["aux", 9], ["aux", 0], ["aux", 0],
    ["kbd", 0x11],
    ["aux", 8], ["aux", 0], ["aux", 0],
    ["kbd", 0x91],
]);

ps2.kbd_send_code(0x1E);
ps2.mouse_send_click(true, false, false);
assert.deepEqual(drain(), [["kbd", 0x1E], ["aux", 9], ["aux", 0], ["aux", 0]]);

// Existing command responses still clear stale device data and are returned first.
ps2.kbd_send_code(0x1E);
ps2.mouse_send_click(false, false, false);
ps2.port64_write(0x20);
assert.deepEqual(drain(), [["kbd", ps2.command_register]]);
