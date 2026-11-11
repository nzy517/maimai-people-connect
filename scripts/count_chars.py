#!/usr/bin/env python3
"""校验加好友留言的字数（含标点），默认上限 50 字。

用法：
  python3 count_chars.py "你好，我是做门店系统的张三，想请教两个新店开业的问题。"
  python3 count_chars.py --limit 60 "第一条" "第二条"
  echo "留言内容" | python3 count_chars.py

计数方式：去掉首尾空白后，每个字符（汉字、字母、数字、标点、中间的空格）都算 1 个。
"""
import sys


def count(text: str) -> int:
    return len(text.strip())


def main(argv):
    limit = 50
    args = list(argv)
    if len(args) >= 2 and args[0] == "--limit":
        limit = int(args[1])
        args = args[2:]
    texts = args if args else [line for line in sys.stdin.read().splitlines() if line.strip()]
    if not texts:
        print(__doc__)
        return 1
    over = 0
    for i, t in enumerate(texts, 1):
        n = count(t)
        status = "OK" if n <= limit else f"超出 {n - limit} 字"
        if n > limit:
            over += 1
        print(f"{i}. {n} 字（上限 {limit}）{status}：{t.strip()}")
    return 1 if over else 0


def _self_test():
    assert count("  你好，世界  ") == 5
    assert count("abc 123") == 7
    assert count("") == 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        _self_test()
        print("self-test passed")
        sys.exit(0)
    sys.exit(main(sys.argv[1:]))
