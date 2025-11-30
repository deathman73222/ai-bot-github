"""Generate professional AI-themed app icon.

Creates icon images suitable for Windows applications.
"""
import os
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Installing Pillow for icon generation...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageDraw, ImageFont


def create_ai_bot_icon() -> None:
    """Create a professional AI Bot icon."""
    output_path = Path(__file__).parent / "ai_bot" / "gui" / "icon.png"
    size = 256
    image = Image.new("RGBA", (size, size), (255, 255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Draw gradient background (blue to purple)
    for y in range(size):
        ratio = y / size
        r = int(0 * (1 - ratio) + 75 * ratio)
        g = int(102 * (1 - ratio) + 0 * ratio)
        b = int(204 * (1 - ratio) + 130 * ratio)
        draw.line([(0, y), (size, y)], fill=(r, g, b, 255))

    # Draw outer circle (white border)
    margin = 10
    draw.ellipse(
        [(margin, margin), (size - margin, size - margin)],
        outline=(255, 255, 255, 255),
        width=3
    )

    # Draw inner circle (brain-like shape center)
    center = size // 2
    radius = size // 4

    # Draw neural network-like pattern
    nodes = [
        (center, center - radius),
        (center + radius, center),
        (center, center + radius),
        (center - radius, center),
        (center, center),
    ]

    # Draw nodes
    node_radius = 8
    for node in nodes:
        draw.ellipse(
            [(node[0] - node_radius, node[1] - node_radius),
             (node[0] + node_radius, node[1] + node_radius)],
            fill=(255, 255, 255, 255),
            outline=(255, 255, 255, 255)
        )

    # Draw connections
    for i, start_node in enumerate(nodes[:-1]):
        for end_node in nodes[i + 1:]:
            draw.line(
                [start_node, end_node],
                fill=(255, 255, 255, 200),
                width=2
            )

    # Draw center highlight (brain core)
    inner_radius = 5
    core = nodes[4]
    draw.ellipse(
        [(core[0] - inner_radius, core[1] - inner_radius),
         (core[0] + inner_radius, core[1] + inner_radius)],
        fill=(255, 215, 0, 255),
        outline=(255, 215, 0, 255)
    )

    # Add lightning bolt effect (AI energy)
    bolt_points = [
        (center - 15, center - 40),
        (center - 5, center - 15),
        (center + 5, center - 15),
        (center + 15, center + 40),
        (center + 5, center + 15),
        (center - 5, center + 15),
    ]
    draw.polygon(bolt_points, fill=(255, 255, 0, 200))

    # Add "AI" text at bottom
    try:
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except Exception:  # pylint: disable=broad-except
            font = ImageFont.load_default()

        text = "AI"
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_x = (size - text_width) // 2
        text_y = size - 50

        draw.text(
            (text_x, text_y),
            text,
            fill=(255, 255, 255, 255),
            font=font
        )
    except Exception:  # pylint: disable=broad-except
        pass

    # Create directory if needed
    os.makedirs(os.path.dirname(str(output_path)), exist_ok=True)

    # Save icon
    image.save(str(output_path), "PNG")
    print(f"✓ AI Bot icon created: {output_path}")

    # Also create ICO format for Windows
    ico_path = str(output_path).replace(".png", ".ico")
    image.save(ico_path, "ICO")
    print(f"✓ Windows icon created: {ico_path}")


def create_installer_icon() -> None:
    """Create icon specifically for the installer."""
    output_path = Path(__file__).parent / "installer_icon.png"
    size = 256
    image = Image.new("RGBA", (size, size), (255, 255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Draw gradient background (green to blue)
    for y in range(size):
        ratio = y / size
        r = int(52 * (1 - ratio) + 0 * ratio)
        g = int(152 * (1 - ratio) + 102 * ratio)
        b = int(219 * (1 - ratio) + 204 * ratio)
        draw.line([(0, y), (size, y)], fill=(r, g, b, 255))

    # Draw installation box/folder
    box_left = size // 4
    box_top = size // 4
    box_right = 3 * size // 4
    box_bottom = 3 * size // 4

    # Folder icon
    draw.rectangle(
        [(box_left, box_top), (box_right, box_bottom)],
        fill=(255, 255, 255, 200),
        outline=(255, 255, 255, 255),
        width=3
    )

    # Checkmark inside
    check_size = (box_right - box_left) // 3
    check_x = (box_left + box_right) // 2
    check_y = (box_top + box_bottom) // 2

    # Draw checkmark
    check_points = [
        (check_x - check_size // 2, check_y),
        (check_x - check_size // 4, check_y + check_size // 2),
        (check_x + check_size // 2, check_y - check_size // 2),
    ]
    draw.line(check_points, fill=(76, 175, 80, 255), width=5)

    os.makedirs(os.path.dirname(str(output_path)), exist_ok=True)
    image.save(str(output_path), "PNG")
    print(f"✓ Installer icon created: {output_path}")


if __name__ == "__main__":
    create_ai_bot_icon()
    create_installer_icon()
