import smbus2

class SSD1306Display:

    # Fundamental Commands
    SSD1306_SET_CONTRAST_CONTROL = 0x81
    SSD1306_DISPLAY_ALL_ON_RESUME = 0xA4
    SSD1306_DISPLAY_ALL_ON = 0xA5
    SSD1306_NORMAL_DISPLAY = 0xA6
    SSD1306_INVERT_DISPLAY = 0xA7
    SSD1306_DISPLAY_OFF = 0xAE
    SSD1306_DISPLAY_ON = 0xAF
    SSD1306_NOP = 0xE3

    # Scrolling Commands
    SSD1306_HORIZONTAL_SCROLL_RIGHT = 0x26
    SSD1306_HORIZONTAL_SCROLL_LEFT = 0x27
    SSD1306_HORIZONTAL_SCROLL_VERTICAL_AND_RIGHT = 0x29
    SSD1306_HORIZONTAL_SCROLL_VERTICAL_AND_LEFT = 0x2A
    SSD1306_DEACTIVATE_SCROLL = 0x2E
    SSD1306_ACTIVATE_SCROLL = 0x2F
    SSD1306_SET_VERTICAL_SCROLL_AREA = 0xA3

    # Addressing Setting Commands
    SSD1306_SET_LOWER_COLUMN = 0x00
    SSD1306_SET_HIGHER_COLUMN = 0x10
    SSD1306_MEMORY_ADDR_MODE = 0x20
    SSD1306_SET_COLUMN_ADDR = 0x21
    SSD1306_SET_PAGE_ADDR = 0x22

    # Hardware Configuration Commands
    SSD1306_SET_START_LINE = 0x40
    SSD1306_SET_SEGMENT_REMAP = 0xA0
    SSD1306_SET_MULTIPLEX_RATIO = 0xA8
    SSD1306_COM_SCAN_DIR_INC = 0xC0
    SSD1306_COM_SCAN_DIR_DEC = 0xC8
    SSD1306_SET_DISPLAY_OFFSET = 0xD3
    SSD1306_SET_COM_PINS = 0xDA
    SSD1306_CHARGE_PUMP = 0x8D

    # Timing & Driving Scheme Setting Commands
    SSD1306_SET_DISPLAY_CLOCK_DIV_RATIO = 0xD5
    SSD1306_SET_PRECHARGE_PERIOD = 0xD9
    SSD1306_SET_VCOM_DESELECT = 0xDB
	
    def __init__(self, width, height, address):
        self.ssd1306_lcd_wid = width
        self.ssd1306_lcd_hei = height
        self.ssd1306_address = address
        self.buffer = bytearray(1024)
        self.font = [
	    0x08, 0x08, 0x20, 0x5f,	# x_size, y_size, offset, number of char
	    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  # <space>
	    0x00,0x00,0x06,0x5f,0x5f,0x06,0x00,0x00,  # !
	    0x00,0x03,0x07,0x00,0x00,0x07,0x03,0x00,  # "
	    0x14,0x7f,0x7f,0x14,0x7f,0x7f,0x14,0x00,  # #
	    0x00,0x24,0x2e,0x6b,0x6b,0x3a,0x12,0x00,  # $
	    0x46,0x66,0x30,0x18,0x0c,0x66,0x62,0x00,  # %
	    0x30,0x7a,0x4f,0x5d,0x37,0x7a,0x48,0x00,  # &
	    0x00,0x00,0x04,0x07,0x03,0x00,0x00,0x00,  # '
	    0x00,0x00,0x1c,0x3e,0x63,0x41,0x00,0x00,  # (
	    0x00,0x00,0x41,0x63,0x3e,0x1c,0x00,0x00,  # )
	    0x08,0x2a,0x3e,0x1c,0x1c,0x3e,0x2a,0x08,  # *		
	    0x00,0x08,0x08,0x3e,0x3e,0x08,0x08,0x00,  # +
	    0x00,0x00,0x80,0xe0,0x60,0x00,0x00,0x00,  # ,
	    0x00,0x08,0x08,0x08,0x08,0x08,0x08,0x00,  # -
	    0x00,0x00,0x00,0x60,0x60,0x00,0x00,0x00,  # .
	    0x60,0x30,0x18,0x0c,0x06,0x03,0x01,0x00,  # /
	
	    0x3e,0x7f,0x51,0x49,0x45,0x7f,0x3e,0x00,  # 0
	    0x00,0x40,0x42,0x7f,0x7f,0x40,0x40,0x00,  # 1
	    0x42,0x63,0x71,0x59,0x49,0x6f,0x66,0x00,  # 2
	    0x22,0x63,0x49,0x49,0x49,0x7f,0x36,0x00,  # 3
	    0x18,0x1c,0x16,0x53,0x7f,0x7f,0x50,0x00,  # 4
	    0x2f,0x6f,0x49,0x49,0x49,0x79,0x31,0x00,  # 5
	    0x3c,0x7e,0x4b,0x49,0x49,0x78,0x30,0x00,  # 6
	    0x03,0x03,0x71,0x79,0x0d,0x07,0x03,0x00,  # 7
	    0x36,0x7f,0x49,0x49,0x49,0x7f,0x36,0x00,  # 8
	    0x06,0x4f,0x49,0x49,0x69,0x3f,0x1e,0x00,  # 9
	    0x00,0x00,0x00,0x66,0x66,0x00,0x00,0x00,  # :
	    0x00,0x00,0x80,0xe6,0x66,0x00,0x00,0x00,  # ;
	    0x00,0x00,0x08,0x1c,0x36,0x63,0x41,0x00,  # <
	    0x00,0x24,0x24,0x24,0x24,0x24,0x24,0x00,  # =
	    0x00,0x41,0x63,0x36,0x1c,0x08,0x00,0x00,  # >
	    0x02,0x03,0x01,0x59,0x5d,0x07,0x02,0x00,  # ?
	
	    0x3e,0x7f,0x41,0x5d,0x5d,0x1f,0x1e,0x00,  # @
	    0x7c,0x7e,0x0b,0x09,0x0b,0x7e,0x7c,0x00,  # A
	    0x41,0x7f,0x7f,0x49,0x49,0x7f,0x36,0x00,  # B
	    0x1c,0x3e,0x63,0x41,0x41,0x63,0x22,0x00,  # C
	    0x41,0x7f,0x7f,0x41,0x63,0x3e,0x1c,0x00,  # D
	    0x41,0x7f,0x7f,0x49,0x5d,0x41,0x63,0x00,  # E
	    0x41,0x7f,0x7f,0x49,0x1d,0x01,0x03,0x00,  # F
	    0x1c,0x3e,0x63,0x41,0x51,0x33,0x72,0x00,  # G
	    0x7f,0x7f,0x08,0x08,0x08,0x7f,0x7f,0x00,  # H
	    0x00,0x00,0x41,0x7f,0x7f,0x41,0x00,0x00,  # I
	    0x30,0x70,0x40,0x41,0x7f,0x3f,0x01,0x00,  # J
	    0x41,0x7f,0x7f,0x08,0x1c,0x77,0x63,0x00,  # K
	    0x41,0x7f,0x7f,0x41,0x40,0x60,0x70,0x00,  # L
	    0x7f,0x7f,0x0e,0x1c,0x0e,0x7f,0x7f,0x00,  # M
	    0x7f,0x7f,0x06,0x0c,0x18,0x7f,0x7f,0x00,  # N
	    0x3e,0x7f,0x41,0x41,0x41,0x7f,0x3e,0x00,  # O
	
	    0x41,0x7f,0x7f,0x49,0x09,0x0f,0x06,0x00,  # P
	    0x3e,0x7f,0x41,0x41,0xe1,0xff,0xbe,0x00,  # Q
	    0x41,0x7f,0x7f,0x09,0x19,0x7f,0x66,0x00,  # R
	    0x22,0x67,0x4d,0x49,0x59,0x73,0x22,0x00,  # S
	    0x00,0x07,0x43,0x7f,0x7f,0x43,0x07,0x00,  # T
	    0x3f,0x7f,0x40,0x40,0x40,0x7f,0x3f,0x00,  # U
	    0x1f,0x3f,0x60,0x40,0x60,0x3f,0x1f,0x00,  # V
	    0x3f,0x7f,0x60,0x38,0x60,0x7f,0x3f,0x00,  # W
	    0x63,0x77,0x1c,0x08,0x1c,0x77,0x63,0x00,  # X
	    0x00,0x07,0x4f,0x78,0x78,0x4f,0x07,0x00,  # Y
	    0x47,0x63,0x71,0x59,0x4d,0x67,0x73,0x00,  # Z
	    0x00,0x00,0x7f,0x7f,0x41,0x41,0x00,0x00,  # [
	    0x01,0x03,0x06,0x0c,0x18,0x30,0x60,0x00,  # <backslash>
	    0x00,0x00,0x41,0x41,0x7f,0x7f,0x00,0x00,  # ]
	    0x08,0x0c,0x06,0x03,0x06,0x0c,0x08,0x00,  # ^
	    0x80,0x80,0x80,0x80,0x80,0x80,0x80,0x80,  # _
	
	    0x00,0x00,0x01,0x03,0x06,0x04,0x00,0x00,  # `
	    0x20,0x74,0x54,0x54,0x3c,0x78,0x40,0x00,  # a
	    0x41,0x7f,0x3f,0x44,0x44,0x7c,0x38,0x00,  # b
	    0x38,0x7c,0x44,0x44,0x44,0x6c,0x28,0x00,  # c
	    0x38,0x7c,0x44,0x45,0x3f,0x7f,0x40,0x00,  # d
	    0x38,0x7c,0x54,0x54,0x54,0x5c,0x18,0x00,  # e
	    0x48,0x7e,0x7f,0x49,0x09,0x03,0x02,0x00,  # f
	    0x98,0xbc,0xa4,0xa4,0xf8,0x7c,0x04,0x00,  # g
	    0x41,0x7f,0x7f,0x08,0x04,0x7c,0x78,0x00,  # h
	    0x00,0x00,0x44,0x7d,0x7d,0x40,0x00,0x00,  # i
	    0x00,0x60,0xe0,0x80,0x80,0xfd,0x7d,0x00,  # j
	    0x41,0x7f,0x7f,0x10,0x38,0x6c,0x44,0x00,  # k
	    0x00,0x00,0x41,0x7f,0x7f,0x40,0x00,0x00,  # l
	    0x7c,0x7c,0x0c,0x78,0x0c,0x7c,0x78,0x00,  # m
	    0x04,0x7c,0x78,0x04,0x04,0x7c,0x78,0x00,  # n
	    0x38,0x7c,0x44,0x44,0x44,0x7c,0x38,0x00,  # o
	
	    0x84,0xfc,0xf8,0xa4,0x24,0x3c,0x18,0x00,  # p
	    0x18,0x3c,0x24,0xa4,0xf8,0xfc,0x84,0x00,  # q
	    0x44,0x7c,0x78,0x4c,0x04,0x0c,0x08,0x00,  # r
	    0x48,0x5c,0x54,0x54,0x54,0x74,0x24,0x00,  # s
	    0x04,0x04,0x3f,0x7f,0x44,0x64,0x20,0x00,  # t
	    0x3c,0x7c,0x40,0x40,0x3c,0x7c,0x40,0x00,  # u
	    0x1c,0x3c,0x60,0x40,0x60,0x3c,0x1c,0x00,  # v
	    0x3c,0x7c,0x60,0x38,0x60,0x7c,0x3c,0x00,  # w
	    0x44,0x6c,0x38,0x10,0x38,0x6c,0x44,0x00,  # x
	    0x9c,0xbc,0xa0,0xa0,0xa0,0xfc,0x7c,0x00,  # y
	    0x00,0x4c,0x64,0x74,0x5c,0x4c,0x64,0x00,  # z
	    0x00,0x08,0x08,0x3e,0x77,0x41,0x41,0x00,  # {
	    0x00,0x00,0x00,0x7f,0x7f,0x00,0x00,0x00,  # |
	    0x00,0x41,0x41,0x77,0x3e,0x08,0x08,0x00,  # }
	    0x02,0x03,0x01,0x03,0x02,0x03,0x01,0x00,  # ~
	]
        self.x_size = 0
        self.y_size = 0
        self.offset = 0
        self.numchars = 0
        self.inverted = 0
        self.I2c_channel = 0
        
        self.LEFT = 0
        self.RIGHT = 254
        self.CENTER = 255
        self.BLACK = 0
        self.WHITE = 1
        self.INVERSE = 2
        self.SSD1306_COMMAND = 0x00
        self.SSD1306_DATA = 0xC0
        self.SSD1306_DATA_CONTINUE = 0x40

    def init(self):
        self.ssd1306_command(self.SSD1306_DISPLAY_OFF)
        self.ssd1306_command(self.SSD1306_SET_DISPLAY_CLOCK_DIV_RATIO)
        self.ssd1306_command(0x80)
        self.ssd1306_command(self.SSD1306_SET_MULTIPLEX_RATIO)
        self.ssd1306_command(self.ssd1306_lcd_hei - 1)
        self.ssd1306_command(self.SSD1306_SET_DISPLAY_OFFSET)
        self.ssd1306_command(0x00)
        self.ssd1306_command(self.SSD1306_SET_START_LINE | 0x00)  # Line: 0
        self.ssd1306_command(self.SSD1306_CHARGE_PUMP)
        self.ssd1306_command(0x14)
        self.ssd1306_command(self.SSD1306_MEMORY_ADDR_MODE)
        self.ssd1306_command(0x00)  # Horizontal Addressing Mode is Used
        self.ssd1306_command(self.SSD1306_SET_SEGMENT_REMAP | 0x01)
        self.ssd1306_command(self.SSD1306_COM_SCAN_DIR_DEC)

        if self.ssd1306_lcd_wid == 128 and self.ssd1306_lcd_hei == 32:
            self.ssd1306_command(self.SSD1306_SET_COM_PINS)
            self.ssd1306_command(0x02)
            self.ssd1306_command(self.SSD1306_SET_CONTRAST_CONTROL)
            self.ssd1306_command(0x8F)
        if self.ssd1306_lcd_wid == 128 and self.ssd1306_lcd_hei == 64:
            self.ssd1306_command(self.SSD1306_SET_COM_PINS)
            self.ssd1306_command(0x12)
            self.ssd1306_command(self.SSD1306_SET_CONTRAST_CONTROL)
            self.ssd1306_command(0xCF)

        self.ssd1306_command(self.SSD1306_SET_PRECHARGE_PERIOD)
        self.ssd1306_command(0xF1)
        self.ssd1306_command(self.SSD1306_SET_VCOM_DESELECT)
        self.ssd1306_command(0x40)
        self.ssd1306_command(self.SSD1306_DISPLAY_ALL_ON_RESUME)
        self.ssd1306_command(self.SSD1306_NORMAL_DISPLAY)
        self.ssd1306_command(self.SSD1306_DEACTIVATE_SCROLL)
        self.ssd1306_command(self.SSD1306_DISPLAY_ON)
        self.clear_display()
        self.set_font()
        self.update()
	 

    def set_font(self):
        self.x_size = self.font[0]
        self.y_size = self.font[1]
        self.offset = self.font[2]
        self.numchars = self.font[3]
        self.inverted = 0

    def write_text(self, x, y, text):
        cnt = 0
        length = len(text)
        if x == "RIGHT":
            x = 128 - (length * self.x_size)
        if x == "CENTER":
            x = (128 - (length * self.x_size)) // 2
        while cnt < length:
            self.write(x + (cnt * self.x_size), y, text[cnt])
            cnt += 1
		
    def write(self, x, y, value):
        font_idx = 0
        rowcnt = 0
        cnt = 0
        temp = 0
        cbyte = 0
        cx = 0
        cy = 0
        cbit = 0
        if self.y_size % 8 == 0:
            font_idx = ((ord(value) - self.offset) * (self.x_size * (self.y_size // 8))) + 4
            for rowcnt in range(self.y_size // 8):
                for cnt in range(self.x_size):
                    temp = self.font[font_idx + cnt + (rowcnt * self.x_size)]
                    for b in range(8):
                        if temp & (1 << b):
                            if not self.inverted:
                                self.draw_pixel(x + cnt, y + (rowcnt * 8) + b, 1)
                            else:
                                self.draw_pixel(x + cnt, y + (rowcnt * 8) + b, 0)
                        else:
                            if not self.inverted:
                                self.draw_pixel(x + cnt, y + (rowcnt * 8) + b, 0)
                            else:
                                self.draw_pixel(x + cnt, y + (rowcnt * 8) + b, 1)
        else:
            font_idx = ((ord(value) - self.offset) * ((self.x_size * self.y_size) // 8)) + 4
            cbyte = self.font[font_idx]
            cbit = 7
            for cx in range(self.x_size):
                for cy in range(self.y_size):
                    if (cbyte & (1 << cbit)) != 0:
                        if not self.inverted:
                            self.draw_pixel(x + cx, y + cy, 1)
                        else:
                            self.draw_pixel(x + cx, y + cy, 0)
                    else:
                        if not self.inverted:
                            self.draw_pixel(x + cx, y + cy, 0)
                        else:
                            self.draw_pixel(x + cx, y + cy, 1)
                    cbit -= 1
                    if cbit < 0:
                        cbit = 7
                        font_idx += 1
                        cbyte = self.font[font_idx]

    def draw_circle(self, x0, y0, r, color):
        f = 1 - r
        ddF_x = 1
        ddF_y = -2 * r
        x = 0
        y = r
        self.draw_pixel(x0, y0 + r, color)
        self.draw_pixel(x0, y0 - r, color)
        self.draw_pixel(x0 + r, y0, color)
        self.draw_pixel(x0 - r, y0, color)
        while x < y:
            if f >= 0:
                y -= 1
                ddF_y += 2
                f += ddF_y
            x += 1
            ddF_x += 2
            f += ddF_x
            self.draw_pixel(x0 + x, y0 + y, color)
            self.draw_pixel(x0 - x, y0 + y, color)
            self.draw_pixel(x0 + x, y0 - y, color)
            self.draw_pixel(x0 - x, y0 - y, color)
            self.draw_pixel(x0 + y, y0 + x, color)
            self.draw_pixel(x0 - y, y0 + x, color)
            self.draw_pixel(x0 + y, y0 - x, color)
            self.draw_pixel(x0 - y, y0 - x, color)
		
    def fill_rectangle(self, x1, y1, x2, y2, color):
        for i in range(x1, x2 + 1):
            self.v_line(y1, y2, i, color)

    def triangle(self, x0, y0, x1, y1, x2, y2, color):
        self.line(x0, y0, x1, y1, color)
        self.line(x1, y1, x2, y2, color)
        self.line(x2, y2, x0, y0, color)

    def rectangle(self, x1, y1, x2, y2, color):
        self.line(x1, y1, x2, y1, color)
        self.line(x1, y2, x2, y2, color)
        self.v_line(y1, y2, x1, color)
        self.v_line(y1, y2, x2, color)

    def v_line(self, y_start, y_end, x_pos, color):
        if y_start > y_end:
            y_start, y_end = y_end, y_start
        while y_start <= y_end:
            self.draw_pixel(x_pos, y_start, color)
            y_start += 1

    def line(self, x_start, y_start, x_end, y_end, color):
        dx = abs(x_end - x_start)
        dy = abs(y_end - y_start)
        x = x_start
        y = y_start
        addx = -1 if x_start > x_end else 1
        addy = -1 if y_start > y_end else 1
        if dx >= dy:
            P = 2 * dy - dx
            for _ in range(dx + 1):
                self.draw_pixel(x, y, color)
                if P < 0:
                    P += 2 * dy
                    x += addx
                else:
                    P += 2 * dy - 2 * dx
                    x += addx
                    y += addy
        else:
            P = 2 * dx - dy
            for _ in range(dy + 1):
                self.draw_pixel(x, y, color)
                if P < 0:
                    P += 2 * dx
                    y += addy
                else:
                    P += 2 * dx - 2 * dy
                    x += addx
                    y += addy

    def draw_pixel(self, x, y, color):
        if (x < 0) or (x >= self.ssd1306_lcd_wid) or (y < 0) or (y >= self.ssd1306_lcd_hei):
            return
        index = x + (y // 8) * self.ssd1306_lcd_wid
        if color == self.WHITE:
            self.buffer[index] |= (1 << (y & 7))
        elif color == self.BLACK:
            self.buffer[index] &= ~(1 << (y & 7))
        elif color == self.INVERSE:
            self.buffer[index] ^= (1 << (y & 7))

    def image(self, image_data):
        for i in range(min(len(self.buffer), len(image_data))):
            self.buffer[i] = image_data[i]

    def update(self):
	    i = 0
	    x = 0
	    self.ssd1306_command(self.SSD1306_SET_COLUMN_ADDR)
	    self.ssd1306_command(0)  # Column start address (0 = reset)
	    self.ssd1306_command(self.ssd1306_lcd_wid - 1)  # Column end address (127 = reset)
	    self.ssd1306_command(self.SSD1306_SET_PAGE_ADDR)
	    self.ssd1306_command(0)  # Page start address (0 = reset)
	    if self.ssd1306_lcd_hei == 64:
	        self.ssd1306_command(7)  # Page end address
	    if self.ssd1306_lcd_hei == 32:
	        self.ssd1306_command(3)  # Page end address
	    if self.ssd1306_lcd_hei == 64:
	        self.ssd1306_command(1)  # Page end address
	    temp = bytearray(16)
	    while i < (self.ssd1306_lcd_wid * self.ssd1306_lcd_hei // 8):
	        for x in range(16):  # for döngüsü 16'ya kadar olmalıdır.
	            temp[x] = self.buffer[i]
	            i += 1
	        self.i2c_write(self.ssd1306_address, [self.SSD1306_DATA_CONTINUE] + list(temp))
					

    def clear_display(self):
        for i in range(len(self.buffer)):
            self.buffer[i] = 0

    def full_display(self):
        for i in range(len(self.buffer)):
            self.buffer[i] = 0xFF

    def ssd1306_command(self, command):
        control = self.SSD1306_COMMAND
        data = [control, command]
        self.i2c_write(self.ssd1306_address, data)

    def ssd1306_data(self, value):
        control = self.SSD1306_DATA
        data = [control, value]
        self.i2c_write(self.ssd1306_address, data)

    def i2c_write(self, address, data):
        with smbus2.SMBus(self.I2c_channel) as bus:
            bus.write_i2c_block_data(address, data[0], data[1:])


import socket
import threading
import signal
import time
import sys

class MyServer:
  
    def __init__(self, host, port, backlog, custom_function=None):
        self.host = host
        self.port = port
        self.backlog = backlog
        self.server_socket = None
        self.running = False
        self.custom_function = custom_function
        self.client_sockets = []  # Bağlı olan tüm client soketlerini saklamak için liste
        self.client_counter = 0

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(self.backlog)

        self.running = True
        self.server_thread = threading.Thread(target=self.server_loop)
        self.server_thread.start()

    def stop(self):
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        if self.server_thread:
            self.server_thread.join()

    def server_loop(self):
        while self.running:
            try:
                client_socket, client_address = self.server_socket.accept()
                self.client_sockets.append(client_socket)  # Yeni client soketini listeye ekle
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                client_thread.start()
                self.client_counter = self.client_counter + 1
            except KeyboardInterrupt:
                self.stop()
                break

    def handle_client(self, client_socket, client_address):
        while True:
            data = client_socket.recv(1024)
            if not data:
                self.client_counter = self.client_counter - 1
                break
            if self.custom_function:
                self.custom_function(data.decode())

        client_socket.close()
        self.client_sockets.remove(client_socket)  # Client soketini listeden kaldır

    def send(self, message):
        for client_socket in self.client_sockets:
            try:
                client_socket.sendall(message.encode())
            except Exception as e:
                print("Error sending message to client:", e)
                
    def get_client_count(self):
 
        return self.client_counter
					
              
def get_ip_address():
    ip_address = ''
    try:
        # Yerel bir bağlantı noktası oluşturarak gerçek IP adresini almayı deneyin
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Google DNS'e bağlanmayı deniyoruz
        ip_address = s.getsockname()[0]
        s.close()
    except Exception as e:
        ip_address=""
    return ip_address

def parse_data(data):
    try:
        data = data[data.index('<') + 1:data.index('>')]
        parts = data.split(',')
        temp_a = parts[0]
        temp_b = ""
        temp_c = ""
        temp_d = ""
        if temp_a == "1":
            temp_b = parts[1]
            temp_c = parts[2]
            temp_d = parts[3]
        return temp_a, temp_b, temp_c, temp_d
    except Exception as e:
        print("Veri ayrıştırma hatası:", e)
        return None, None, None, None

def print_ip():
    my_ip = get_ip_address()
    display.clear_display()
    display.write_text(0,8,my_ip)
    display.update()

def data_arrived(data):
    global server
    received_message = data
    received_message = received_message.replace('(', '<')
    received_message = received_message.replace(')', '>')
    temp_a, temp_b, temp_c , temp_d = parse_data(received_message)
    if temp_a is not None and temp_b is not None and temp_c is not None:
        if temp_a == "0":
            display.clear_display()
        if temp_a == "1":
            display.write_text(int(temp_b),int(temp_c),temp_d)
        if temp_a == "2":
            display.update()
        if temp_a == "9":
            print_ip()
	
server = MyServer('0.0.0.0', 12344, 5, custom_function=data_arrived)  	
display = SSD1306Display(128, 32, 0x3C)
 
def main():
    display.init()    
    while True:
        ip_find = get_ip_address().find("192.168")
        if ip_find != -1:
            break
        else:
            time.sleep(0.5)
    print("OLED PROG. STARTED")
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    server.start()
    while True:
        time.sleep(0.1)
        if server.get_client_count() == 0:
            print_ip()
	          

if __name__ == "__main__":
    main()
