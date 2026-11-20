import json
import os
from datetime import datetime


class ClaudeMemory:
    def __init__(self, file_path: str = "ai_studio/memories.json"):
        self.file_path = file_path
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=2)

    def add_memory(self, content: str, tag: str = "general"):
        memories = self.get_all()
        memories.append({
            "timestamp": datetime.now().isoformat(),
            "tag": tag,
            "content": content,
        })
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(memories, f, ensure_ascii=False, indent=2)

    def get_all(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            return json.load(f)


if __name__ == "__main__":
    mem = ClaudeMemory()
    mem.add_memory("เริ่มต้นใช้งานระบบความจำสำหรับ Claude", tag="init")
    print("บันทึกความจำเรียบร้อย:", mem.get_all())
