# Color Convert Python

[![PyPI Version](https://img.shields.io/pypi/v/color-convert-python?style=flat-square)](https://pypi.org/project/color-convert-python/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/color-convert-python?style=flat-square)](https://pypi.org/project/color-convert-python/)
[![License](https://img.shields.io/pypi/l/color-convert-python?style=flat-square)](LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/color-convert-python?style=flat-square)](https://pypi.org/project/color-convert-python/)
[![GitHub Stars](https://img.shields.io/github/stars/mizoz/color-convert-python?style=flat-square)](https://github.com/mizoz/color-convert-python)

> A Python CLI tool for converting between HEX and RGB color formats with ease.

## Features

- Convert HEX to RGB
- Convert RGB to HEX
- Support for RGB and RGBA formats
- Batch color conversion
- Command-line interface
- Python API for integration

## Installation

### From PyPI

```bash
pip install color-convert-python
```

### From Source

```bash
git clone https://github.com/mizoz/color-convert-python.git
cd color-convert-python
pip install -e .
```

## Usage

### Command Line

```bash
# Convert HEX to RGB
color-convert "#FF5733"

# Convert RGB to HEX
color-convert "rgb(255, 87, 51)"

# Convert with alpha
color-convert "rgba(255, 87, 51, 0.5)"
```

### Python API

```python
from color_convert import ColorConverter

converter = ColorConverter()

# HEX to RGB
rgb = converter.hex_to_rgb("#FF5733")
print(rgb)  # (255, 87, 51)

# RGB to HEX
hex_color = converter.rgb_to_hex(255, 87, 51)
print(hex_color)  # #FF5733
```

## CLI Options

| Option | Description |
|--------|-------------|
| `-r, --rgb` | Input as RGB format |
| `-x, --hex` | Input as HEX format |

## Requirements

- Python 3.7+

## Contributing

Contributions are welcome! Please feel free to submit a [Pull Request](https://github.com/mizoz/color-convert-python/pulls).

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**mizoz**
- GitHub: [@mizoz](https://github.com/mizoz)

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
