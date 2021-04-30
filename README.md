# CLI-Colors
A light-weight library for accessible terminal colors.

This is mainly taken from this [Stack Overflow answer](https://stackoverflow.com/a/33206814)


# Usage
The library provides a single function `color_print` and a handful of named colors and modifiers.

To use `color_print`, pass the text to be printed, the color of the text, and a list of modifiers.

## Examples

```python
# Print yellow text
color_print("Yellow Text\n", YELLOW)

# Print blue bold crossed-out text
color_print("Blue Text\n", BLUE, MOD_BOLD, MOD_CROSS_OUT)

# Print using an RGB color
color_print("RGB Text\n", (255, 255, 100))

# Pass a custom 8-bit color
color_print("Custom 8-bit Text\n", MOD_8BIT + "52", MOD_ITALIC)
```
![](examples.png)