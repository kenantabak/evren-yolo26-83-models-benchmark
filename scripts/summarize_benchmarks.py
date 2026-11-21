#!/usr/bin/env python3
"""Summarize benchmark metrics across 83 PRODUCTION YOLO26/YOLO11 models."""
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean, median


def main() -> None:
    csv_path = Path(__file__).resolve().parents[1] / "data" / "models_benchmark_83.csv"
    by_arch = defaultdict(list)
    with open(csv_path, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            by_arch[r["architecture"]].append(float(r["mAP50_percent"]))

    print(f"{'Architecture':12s} | {'Count':>5s} | {'Mean mAP@50':>11s} | {'Median':>8s} | {'Max':>8s}")
    print("-" * 55)
    for arch, vals in sorted(by_arch.items()):
        print(f"{arch:12s} | {len(vals):5d} | {mean(vals):10.2f}% | {median(vals):7.2f}% | {max(vals):7.2f}%")


if __name__ == "__main__":
    main()
