#!/usr/bin/env python3
"""Tiny self-check for the Ganhuo Travel Lock skill contract."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def must_contain(path, needles):
    text = (ROOT / path).read_text(encoding="utf-8")
    missing = [needle for needle in needles if needle not in text]
    if missing:
        raise SystemExit(f"{path} missing: {', '.join(missing)}")


def main():
    must_contain("SKILL.md", [
        "booking-lockin-workflow.md",
        "price-verification-workflow.md",
        "实时核验证据表",
        "Do not auto-submit orders",
        "bypass captchas",
        "已锁定",
    ])
    must_contain("references/booking-lockin-workflow.md", [
        "Decision Log",
        "The agent must not",
        "Auto-submit orders",
    ])
    must_contain("references/price-verification-workflow.md", [
        "queried_at",
        "Source Priority",
        "Price seen",
        "查到的当前价",
    ])
    must_contain("references/travel-guide-template.md", [
        "旅行锁定卡",
        "订前决策支持",
        "未定目的地时只给 3 个差异化方案",
        "不写未经核验的票价",
    ])
    print("ganhuo travel lock self-check ok")


if __name__ == "__main__":
    main()
