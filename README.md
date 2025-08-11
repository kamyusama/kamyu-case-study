\# Kamyu Case Study — Twitch→LLM→TTS→(字幕) Minimal Demo



> ⚠️ \*\*非商用デモのみ\*\*。商用利用・再配布は禁止。販売版の実装は含みません。



\## TL;DR

\- Twitchコメントを\*\*模擬イベント\*\*で受け取り → 簡易応答を生成 → （任意）OBSへ字幕を\*\*1回だけ\*\*送る最小デモ。

\- 目的：\*\*実装力の証明\*\*（構成・最小コード）。\*\*商用版の中身は公開しない\*\*。



\## Architecture

```mermaid

flowchart LR

&nbsp; A\[Twitch (Mock Event)] --> B\[Python Minimal App]

&nbsp; B --> C\[Reply Generator (Mock)]

&nbsp; C -->|optional| D\[OBS WebSocket: Caption Once]



Quickstart

bash
コピーする
編集する
# Windows
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python src/main.py
# 任意：ダミー送信
python src/optional_obs_caption.py
License

License
See LICENSE-SAMPLE.md（デモ用途限定・商用不可）。