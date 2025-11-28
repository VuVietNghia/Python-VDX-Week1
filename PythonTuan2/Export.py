import os

def export_txt_to_desktop():
    desktop_path = "/home/nghiavu/Desktop"
    output_file = os.path.join(desktop_path, "tệp.txt")
    
    content = "Hê lô thế giới."
    
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully exported file to: {output_file}")
    except Exception as e:
        print(f"Failed to export file: {e}")

if __name__ == "__main__":
    export_txt_to_desktop()
