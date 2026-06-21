# -*- coding: utf-8 -*-
"""Regenerate portfolio with lang-aware links and updated email."""
from __future__ import annotations

import importlib.util
from pathlib import Path

BASE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("u", BASE / "update_i18n.py")
u = importlib.util.module_from_spec(spec)
spec.loader.exec_module(u)

EMAIL = "alexandero.mobile@gmail.com"
GH = "https://github.com/alexanderomobile"


def readme_name(lang: str) -> str:
    return "README.md" if lang == "ru" else f"README.{lang}.md"


def repo_readme_url(slug: str, lang: str) -> str:
    return f"{GH}/{slug}/blob/main/{readme_name(lang)}"


def portfolio_readme_url(lang: str) -> str:
    return f"{GH}/portfolio/blob/main/{readme_name(lang)}"


def portfolio_tree_url(lang: str) -> str:
    return f"{GH}/portfolio/tree/main/case-studies/{lang}"


def case_study_url(case_file: str, lang: str) -> str:
    return f"{GH}/portfolio/blob/main/case-studies/{lang}/{case_file}"


def pages_url(lang: str) -> str:
    if lang == "ru":
        return "https://alexanderomobile.github.io/portfolio/"
    return f"https://alexanderomobile.github.io/portfolio/{lang}.html"


def showcase_readme_full(slug: str, lang: str, case_file: str) -> str:
    p = u.PROJECTS[slug][lang]
    labels = {
        "ru": ("Задача", "Функционал", "Польза для бизнеса", "Стек", "Архитектура", "Запуск", "Статус", "Завершён", "Case Study"),
        "en": ("Problem", "Features", "Business value", "Stack", "Architecture", "Run", "Status", "Production-ready", "Case Study"),
        "es": ("Problema", "Funcionalidad", "Valor de negocio", "Stack", "Arquitectura", "Ejecución", "Estado", "En producción", "Case Study"),
    }[lang]
    private = {
        "ru": "Showcase без кода. Исходники — приватный репозиторий.",
        "en": "Showcase only (no source code). Code in a private repository.",
        "es": "Showcase sin código. Fuentes en repositorio privado.",
    }[lang]
    cs = case_study_url(case_file, lang)
    stacks = {
        "rag-documentation-assistant": "Python · OpenAI · ChromaDB · SQLite · RAGAS",
        "partio-bot": "Python · aiogram 3 · FastAPI · SQLAlchemy · MySQL",
        "p2p-bybit-optimum": "aiogram 3 · FastAPI · Bybit API · Gemini · MySQL",
        "optimum-real-estate-bot": "python-telegram-bot · MySQL · ChromaDB · OpenAI · WordPress",
        "muzloprom-ai-clips": "FastAPI · aiogram · MySQL · OpenAI · Qwen WAN · ffmpeg",
    }[slug]
    runs = {
        "rag-documentation-assistant": "pip install -r requirements.txt && python app.py",
        "partio-bot": 'pip install -e ".[dev]" && partiobot',
        "p2p-bybit-optimum": "pip install -r requirements.txt && python run.py",
        "optimum-real-estate-bot": "pip install -r requirements.txt && python main.py",
        "muzloprom-ai-clips": "uvicorn app.main:app --host 0.0.0.0 --port 8100",
    }[slug]
    asset = u.fix_asset_path(slug)
    L = labels
    return f"""{u.LANG_BAR[lang]}

# {p['title']}

**{p['tagline']}**

> {private}

---

## {L[0]}

{p['tagline']}.

## {L[1]}

{p['func']}

## {L[2]}

{p['biz']}

## {L[3]}

{stacks}

## {L[4]}

![Architecture](assets/{asset})

## {L[5]}

```bash
{runs}
```

**{L[6]}:** ✅ {L[7]}

**{L[8]}:** [{case_file}]({cs})

[@alexanderomobile]({GH})
"""


def case_study(name: str, lang: str) -> str:
    slug = u.CASE_MAP[name]
    p = u.PROJECTS[slug][lang]
    L = {
        "ru": ("Задача", "Функционал", "Польза для бизнеса", "Стек", "Функциональные блоки", "Скриншоты", "Запуск", "К портфолио"),
        "en": ("Problem", "Features", "Business value", "Stack", "Modules", "Screenshots", "Run", "Back to portfolio"),
        "es": ("Problema", "Funcionalidad", "Valor de negocio", "Stack", "Módulos", "Capturas", "Ejecución", "Volver al portfolio"),
    }[lang]
    showcase = repo_readme_url(slug, lang)
    asset = u.fix_asset_path(slug)
    return f"""# Case Study: {p['title']}

**Showcase:** [{slug}]({showcase})
**Status:** ✅ Production

---

## {L[0]}

{p['tagline']}.

## {L[1]}

{p['func']}

## {L[2]}

{p['biz']}

## {L[3]}

See showcase README.

## {L[4]}

Ingest · Search · Delivery · Integrations

## {L[5]}

![Architecture](../../assets/{asset})

## {L[6]}

See showcase README for run instructions.

---

[← {L[7]}]({portfolio_readme_url(lang)})
"""


def profile(lang: str) -> str:
    titles = {
        "ru": ("Александр · Prompt/Context Engineer & AI Automation", "Промпт/контекст-инженер и разработчик ботов", "Компетенции", "Избранные проекты", "Проект", "Польза для бизнеса", "Опыт RAG-проектов", "Полный цикл: vector store → ETL → delivery → RAGAS → optimization.", "Case studies", "Контакты"),
        "en": ("Alexander · Prompt/Context Engineer & AI Automation", "Prompt/context engineer and bot developer", "Skills", "Projects", "Project", "Business value", "RAG experience", "Full cycle: vector store → ETL → delivery → RAGAS → optimization.", "Case studies", "Contact"),
        "es": ("Alexander · Prompt/Context Engineer & AI Automation", "Ingeniero prompt/contexto y desarrollador de bots", "Competencias", "Proyectos", "Proyecto", "Valor de negocio", "Experiencia RAG", "Ciclo completo: vector store → ETL → delivery → RAGAS → optimization.", "Case studies", "Contacto"),
    }[lang]
    rows = [
        f"| [{u.PROJECTS[s][lang]['title']}]({repo_readme_url(s, lang)}) | {u.PROJECTS[s][lang]['biz']} |"
        for _, s in u.CASE_MAP.items()
    ]
    return f"""# {titles[0]}

**{titles[1]}** — RAG, LLM, automation.

---

## {titles[2]}

RAG · LLM APIs · Telegram bots · n8n · Python · FastAPI · MySQL

---

## {titles[3]}

| {titles[4]} | {titles[5]} |
|--------|-------------------|
{chr(10).join(rows)}
| [Portfolio]({portfolio_readme_url(lang)}) | {titles[8]} RU / EN / ES |

---

## {titles[6]}

{titles[7]}

[{titles[8]}]({portfolio_tree_url(lang)})

---

## {titles[9]}

- **GitHub:** [@alexanderomobile]({GH})
- **Telegram:** [@alexandero_spb](https://t.me/alexandero_spb)
- **Email:** {EMAIL}

---

## GitHub Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=alexanderomobile&show_icons=true&theme=default&hide_border=true)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=alexanderomobile&layout=compact&theme=default&hide_border=true)
"""


def portfolio_readme(lang: str) -> str:
    titles = {
        "ru": ("Portfolio · Case Studies", "Публичное портфолио на трёх языках.", "Проекты", "Польза для бизнеса"),
        "en": ("Portfolio · Case Studies", "Public portfolio in three languages.", "Projects", "Business value"),
        "es": ("Portfolio · Case Studies", "Portafolio público en tres idiomas.", "Proyectos", "Valor de negocio"),
    }[lang]
    rows = []
    for cf, slug in u.CASE_MAP.items():
        p = u.PROJECTS[slug][lang]
        biz = p["biz"] if len(p["biz"]) <= 90 else p["biz"][:90] + "…"
        rows.append(f"| [{p['title']}](case-studies/{lang}/{cf}) | {biz} |")
    return f"""{u.LANG_BAR[lang]}

# {titles[0]}

{titles[1]}

**GitHub Pages:** {pages_url(lang)}

---

## {titles[2]}

| Case study | {titles[3]} |
|------------|----------------|
{chr(10).join(rows)}

[@alexanderomobile]({GH})
"""


def extra_case(cf: str, lang: str, title: str, func: str, biz: str) -> str:
    label = {"ru": "Польза для бизнеса", "en": "Business value", "es": "Valor de negocio"}[lang]
    back = {"ru": "К портфолио", "en": "Back to portfolio", "es": "Volver al portfolio"}[lang]
    return f"""# Case Study: {title}

## Features

{func}

## {label}

{biz}

---

[← {back}]({portfolio_readme_url(lang)})
"""


def main() -> None:
    for lang, suffix in [("ru", ""), ("en", ".en"), ("es", ".es")]:
        u.w(f"alexanderomobile/README{suffix}.md", u.LANG_BAR[lang] + "\n\n" + profile(lang))
        u.w(f"portfolio/README{suffix}.md", portfolio_readme(lang))

    for lang in ("ru", "en", "es"):
        for cf, slug in u.CASE_MAP.items():
            u.w(f"portfolio/case-studies/{lang}/{cf}", case_study(cf, lang))

    extra = {
        "06-telegram-knowledge-bot.md": {
            "ru": ("Telegram Knowledge Bot", "RAG-бот по базе знаний с памятью диалога.", "Снижает время ответа сотрудникам и клиентам в Telegram."),
            "en": ("Telegram Knowledge Bot", "RAG bot with session memory.", "Faster answers for staff and clients in Telegram."),
            "es": ("Telegram Knowledge Bot", "Bot RAG con memoria de sesión.", "Respuestas más rápidas en Telegram."),
        },
        "07-rag-platform.md": {
            "ru": ("RAG Platform", "Полный цикл: хранилище → ETL → delivery → RAGAS → optimization.", "Снижает cost/latency production RAG и повышает качество ответов."),
            "en": ("RAG Platform", "Full cycle: storage → ETL → delivery → RAGAS → optimization.", "Lowers RAG cost/latency and improves answer quality."),
            "es": ("RAG Platform", "Ciclo completo: almacén → ETL → delivery → RAGAS → optimización.", "Reduce costo/latencia RAG y mejora calidad."),
        },
    }
    for cf, data in extra.items():
        for lang in ("ru", "en", "es"):
            t, f, b = data[lang]
            u.w(f"portfolio/case-studies/{lang}/{cf}", extra_case(cf, lang, t, f, b))

    for cf, slug in u.CASE_MAP.items():
        for lang, suffix in [("ru", ""), ("en", ".en"), ("es", ".es")]:
            u.w(f"{slug}/README{suffix}.md", showcase_readme_full(slug, lang, cf))

    for lang, fname in [("ru", "index.html"), ("en", "en.html"), ("es", "es.html")]:
        cards = []
        for cf, slug in u.CASE_MAP.items():
            p = u.PROJECTS[slug][lang]
            lbl = {"ru": "Польза", "en": "Value", "es": "Valor"}[lang]
            func = p["func"] if len(p["func"]) <= 100 else p["func"][:100] + "…"
            biz = p["biz"] if len(p["biz"]) <= 120 else p["biz"][:120] + "…"
            cards.append(
                f'<article class="card"><h2>{p["title"]}</h2><p>{func}</p>'
                f'<p><strong>{lbl}:</strong> {biz}</p>'
                f'<a href="{repo_readme_url(slug, lang)}">Showcase →</a></article>'
            )
        h1 = {"ru": "Prompt Engineer Portfolio", "en": "Prompt Engineer Portfolio", "es": "Portafolio Prompt Engineer"}[lang]
        sub = {"ru": "Портфолио", "en": "Portfolio", "es": "Portafolio"}[lang]
        link = {"ru": "Все case studies →", "en": "All case studies →", "es": "Todos los case studies →"}[lang]
        html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{h1}</title>
<style>:root{{--bg:#0d1117;--card:#161b22;--text:#c9d1d9;--accent:#58a6ff;--muted:#8b949e}}body{{font-family:system-ui,sans-serif;background:var(--bg);color:var(--text);margin:0}}.wrap{{max-width:960px;margin:0 auto;padding:2rem}}.grid{{display:grid;gap:1rem;grid-template-columns:repeat(auto-fill,minmax(280px,1fr))}}.card{{background:var(--card);border:1px solid #30363d;border-radius:12px;padding:1.25rem}}a{{color:var(--accent)}}.nav{{margin-bottom:1.5rem;color:var(--muted)}}</style></head>
<body><div class="wrap"><p class="nav">🇷🇺 <a href="index.html">RU</a> · 🇬🇧 <a href="en.html">EN</a> · 🇪🇸 <a href="es.html">ES</a></p>
<h1>{h1}</h1><p>{sub} · <a href="{GH}">@alexanderomobile</a></p>
<div class="grid">{''.join(cards)}
<article class="card"><h2>Case Studies</h2><a href="{portfolio_tree_url(lang)}">{link}</a></article>
</div></div></body></html>"""
        u.w(f"portfolio/docs/{fname}", html)

    print("Done:", EMAIL)


if __name__ == "__main__":
    main()
