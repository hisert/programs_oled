byte_array = [
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfc, 0x7f, 0xff, 0x8c, 0x7f, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfc, 0x7f, 0xff, 0x8c, 0x7f, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfc, 0x7f, 0xff, 0x8c, 0x7f, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xf0, 0x3f, 0x87, 0xc1, 0xf0, 0x60, 0x0f, 0xc0, 0x40, 0x7f, 0xe1, 0xf8, 0x01, 0xf0, 0xf8, 0xf0, 
	0xe0, 0x0f, 0x87, 0xc1, 0xf0, 0x60, 0x0f, 0xc0, 0x40, 0x7f, 0x80, 0x78, 0x01, 0xf0, 0xf8, 0xe1, 
	0xc0, 0x1f, 0x03, 0xc0, 0xe0, 0x60, 0x0f, 0xc0, 0x40, 0x7f, 0x00, 0x38, 0x01, 0xe0, 0x78, 0xe3, 
	0x87, 0xbf, 0x03, 0xc0, 0xe0, 0x63, 0xff, 0xc0, 0x40, 0x7e, 0x1e, 0x1f, 0xe3, 0xe0, 0x78, 0xc3, 
	0x8f, 0xff, 0x03, 0xc0, 0xe0, 0x63, 0xff, 0xff, 0xff, 0xfe, 0x3f, 0x1f, 0xc3, 0xe0, 0x78, 0x87, 
	0x1f, 0xfe, 0x31, 0xc0, 0x40, 0x63, 0xff, 0xf8, 0x7f, 0xfc, 0x7f, 0x8f, 0x87, 0xc6, 0x38, 0x8f, 
	0x1f, 0xfe, 0x31, 0xc0, 0x40, 0x60, 0x3f, 0xf8, 0x7f, 0xfc, 0x7f, 0x8f, 0x87, 0xc6, 0x38, 0x1f, 
	0x1f, 0xfe, 0x31, 0xc4, 0x44, 0x60, 0x3f, 0xf8, 0x7f, 0xfc, 0x7f, 0x8f, 0x0f, 0xc6, 0x38, 0x1f, 
	0x1f, 0xfe, 0x31, 0xc4, 0x04, 0x60, 0x3f, 0xf8, 0x43, 0xfc, 0x7f, 0x8e, 0x1f, 0xc6, 0x38, 0x0f, 
	0x1f, 0xfc, 0x00, 0xc4, 0x04, 0x63, 0xff, 0xf8, 0x43, 0xfc, 0x7f, 0x8e, 0x1f, 0x80, 0x18, 0x8f, 
	0x8f, 0xfc, 0x00, 0xc6, 0x0c, 0x63, 0xff, 0xf8, 0x43, 0xfe, 0x3f, 0x1c, 0x3f, 0x80, 0x18, 0x87, 
	0x87, 0xbc, 0x00, 0xc6, 0x0c, 0x63, 0xff, 0xf8, 0x43, 0xfe, 0x1e, 0x1c, 0x7f, 0x80, 0x18, 0xc3, 
	0xc0, 0x1c, 0x78, 0xc6, 0x0c, 0x60, 0x0f, 0xff, 0xc3, 0xff, 0x00, 0x38, 0x01, 0x8f, 0x18, 0xe1, 
	0xe0, 0x08, 0xfc, 0x47, 0x1c, 0x60, 0x0f, 0xff, 0xc3, 0xff, 0x80, 0x78, 0x01, 0x1f, 0x88, 0xf1, 
	0xf8, 0x38, 0xfc, 0x47, 0x1c, 0x60, 0x0f, 0xff, 0xc3, 0xff, 0xe1, 0xf8, 0x01, 0x1f, 0x88, 0xf0, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
]
