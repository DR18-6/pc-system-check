"""Collect basic system information and save a readable report."""

import platform
import socket
from datetime import datetime
from pathlib import Path


def get_system_info():
    """Return basic information about the computer running this script."""
    return {
        "Operating system": platform.system(),
        "OS version": platform.version(),
        "Machine architecture": platform.machine(),
        "Processor": platform.processor() or "Not available",
        "Python version": platform.python_version(),
        "Computer name": socket.gethostname(),
        "Report created": datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z"),
    }


def format_report(info):
    """Format the collected information as readable text."""
    lines = ["PC SYSTEM CHECK", "=" * 40]
    lines.extend(f"{label}: {value}" for label, value in info.items())
    return "\n".join(lines) + "\n"


def save_report(report, filename="system_report.txt"):
    """Write the report to a UTF-8 text file."""
    output_path = Path(filename)
    output_path.write_text(report, encoding="utf-8")
    return output_path


def main():
    """Run the system check and show where the report was saved."""
    print("Collecting basic system information...\n")

    try:
        info = get_system_info()
        report = format_report(info)
        print(report)
        output_path = save_report(report)
        print(f"Report saved to: {output_path.resolve()}")
    except OSError as error:
        print(f"Could not save the report: {error}")


if __name__ == "__main__":
    main()
