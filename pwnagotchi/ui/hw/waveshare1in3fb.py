import logging
import time

import pwnagotchi.ui.fonts as fonts
from pwnagotchi.ui.hw.base import DisplayImpl

log = logging.getLogger(__name__)


class WaveShare1in3FB(DisplayImpl):
    def __init__(self, config):
        super(WaveShare1in3FB, self).__init__(config, 'waveshare1in3fb')

    def layout(self):
        fonts.setup(12, 10, 12, 70, 25, 9)
        self._layout['width'] = 240
        self._layout['height'] = 240
        self._layout['face'] = (35, 50)
        self._layout['name'] = (5, 20)
        self._layout['channel'] = (0, 0)
        self._layout['aps'] = (40, 0)
        self._layout['uptime'] = (180, 0)
        self._layout['line1'] = [0, 14, 240, 14]
        self._layout['line2'] = [0, 220, 240, 220]
        self._layout['friend_face'] = (0, 130)
        self._layout['friend_name'] = (40, 135)
        self._layout['shakes'] = (0, 220)
        self._layout['mode'] = (200, 220)
        self._layout['status'] = {
            'pos': (80, 160),
            'font': fonts.status_font(fonts.Medium),
            'max': 20
        }

        return self._layout

    def refresh(self):
        time.sleep(0.1)

    def initialize(self):
        from pwnagotchi.ui.hw.libs.fb import fb
        self._display = fb
        log.info("initializing Waveshare 1.3\" LCD (240x240) via framebuffer")
        self._display.ready_fb(i=1)  # Use /dev/fb1
        self._display.black_scr()

    def render(self, canvas):
        self._display.show_img(canvas)
        self.refresh()

    def clear(self):
        self._display.black_scr()
        self.refresh()
