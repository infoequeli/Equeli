"""Equeli – preproste linijske ikone (24 × 24, tanka črta). Uporaba: icon("compass")."""

P = {
    "family": '<circle cx="8" cy="7" r="3"/><circle cx="17" cy="9" r="2.4"/><path d="M2.5 20c0-3.3 2.5-6 5.5-6s5.5 2.7 5.5 6"/><path d="M14.5 20c0-2.6 1.2-4.6 2.5-4.6s3 2 3 4.6"/>',
    "school": '<path d="M3 10l9-5 9 5"/><path d="M5 10v9h14v-9"/><path d="M10 19v-5h4v5"/>',
    "compass": '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
    "book": '<path d="M4 5.5C4 4.7 4.7 4 5.5 4H11v16H5.5c-.8 0-1.5-.7-1.5-1.5z"/><path d="M20 5.5c0-.8-.7-1.5-1.5-1.5H13v16h5.5c.8 0 1.5-.7 1.5-1.5z"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "message": '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9.5h8M8 12.5h5"/>',
    "shield": '<path d="M12 3l8 3v6c0 4.5-3.4 8.2-8 9-4.6-.8-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    "chart": '<path d="M3 20h18"/><path d="M6 20v-7M11 20V6M16 20V10M20 20v-4"/>',
    "article": '<path d="M5 4h10l4 4v12H5z"/><path d="M15 4v4h4"/><path d="M8 12h8M8 16h6"/>',
    "heart": '<path d="M12 20s-8-4.8-8-10.2A4.3 4.3 0 0 1 12 7a4.3 4.3 0 0 1 8 2.8C20 15.2 12 20 12 20z"/>',
    "link": '<path d="M9 15l6-6"/><path d="M11 6.5l1.5-1.5a4 4 0 0 1 5.7 5.7L16.7 12"/><path d="M13 17.5L11.5 19a4 4 0 0 1-5.7-5.7L7.3 12"/>',
    "grid": '<rect x="4" y="4" width="6.5" height="6.5" rx="1.5"/><rect x="13.5" y="4" width="6.5" height="6.5" rx="1.5"/><rect x="4" y="13.5" width="6.5" height="6.5" rx="1.5"/><rect x="13.5" y="13.5" width="6.5" height="6.5" rx="1.5"/>',
    "move": '<circle cx="12" cy="4.5" r="2"/><path d="M12 7v6l-3 7M12 13l3 7M7 10h10"/>',
    "target": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1"/>',
    "people": '<circle cx="8" cy="8" r="2.5"/><circle cx="16" cy="8" r="2.5"/><path d="M3.5 19c0-3 2-5 4.5-5 1.6 0 3 .8 4 2 1-1.2 2.4-2 4-2 2.5 0 4.5 2 4.5 5"/>',
    "leaf": '<path d="M5 19C5 10 10 5 20 4c-1 10-6 15-15 15z"/><path d="M5 19l8-8"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/>',
    "search": '<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/>',
    "clipboard": '<rect x="5" y="4.5" width="14" height="16" rx="2"/><path d="M9 4.5V3h6v1.5"/><path d="M9 10h6M9 14h6"/>',
    "euro": '<path d="M17 6.5A6.5 6.5 0 1 0 17 17.5"/><path d="M4.5 10.5h9M4.5 13.5h9"/>',
    "box": '<path d="M3.5 7.5L12 3l8.5 4.5v9L12 21l-8.5-4.5z"/><path d="M3.5 7.5L12 12l8.5-4.5M12 12v9"/>',
    "mic": '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5.5 11a6.5 6.5 0 0 0 13 0M12 17.5V21"/>',
    "camera": '<path d="M4 8h3l2-2.5h6L17 8h3v11H4z"/><circle cx="12" cy="13" r="3.5"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
}


def icon(name, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{P[name]}</svg>'


def badge(name, cls=""):
    return f'<span class="ic-wrap {cls}">{icon(name)}</span>'
