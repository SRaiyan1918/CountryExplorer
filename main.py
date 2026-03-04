import streamlit as st
import requests

# ============================================================
#   COUNTRY INFO APP — Maximum Data Display
#   Run: streamlit run country_app.py
#   API: restcountries.com — No API key needed!
# ============================================================

st.set_page_config(
    page_title="Country Explorer",
    page_icon="🌍",
    layout="wide"
)

# ── CSS ───────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;600;700&family=Syne:wght@400;700;800&display=swap');

.stApp {
    background: linear-gradient(135deg, #0a0a0f 0%, #0d1117 50%, #0a0f1a 100%);
    font-family: 'JetBrains Mono', monospace;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem; }

/* Title */
.main-title {
    font-family: 'Syne', sans-serif;
    font-size: 2.5rem;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(90deg, #00d4ff, #00ffcc, #00d4ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 5px;
    margin-bottom: 0.2rem;
}
.main-subtitle {
    text-align: center;
    color: #4a5568;
    font-size: 0.7rem;
    letter-spacing: 3px;
    margin-bottom: 1.5rem;
}

/* Section headers */
.section-header {
    font-family: 'Syne', sans-serif;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 3px;
    color: #00d4ff;
    text-transform: uppercase;
    border-bottom: 1px solid rgba(0,212,255,0.2);
    padding-bottom: 0.5rem;
    margin: 1.5rem 0 1rem 0;
}

/* Cards */
.info-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.7rem;
    transition: border-color 0.3s;
}
.info-card:hover { border-color: rgba(0,212,255,0.25); }

.card-label {
    font-size: 0.65rem;
    color: #4a5568;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 0.3rem;
}
.card-value {
    font-size: 1rem;
    color: #e2e8f0;
    font-weight: 600;
}
.card-value-large {
    font-size: 1.4rem;
    font-weight: 700;
    color: #00d4ff;
}

/* Country hero */
.country-hero {
    background: linear-gradient(135deg, rgba(0,212,255,0.07), rgba(0,255,204,0.04));
    border: 1px solid rgba(0,212,255,0.15);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin-bottom: 1.5rem;
}
.country-flag-emoji { font-size: 4rem; }
.country-name-hero {
    font-family: 'Syne', sans-serif;
    font-size: 2.2rem;
    font-weight: 800;
    color: #ffffff;
    margin: 0.5rem 0 0.2rem;
}
.country-official {
    color: #718096;
    font-size: 0.8rem;
    letter-spacing: 1px;
}

/* Tag pills */
.tag {
    display: inline-block;
    background: rgba(0,212,255,0.1);
    border: 1px solid rgba(0,212,255,0.2);
    border-radius: 999px;
    padding: 0.2rem 0.8rem;
    font-size: 0.75rem;
    color: #00d4ff;
    margin: 0.2rem;
}
.tag-green {
    background: rgba(72,187,120,0.1);
    border-color: rgba(72,187,120,0.2);
    color: #68d391;
}
.tag-yellow {
    background: rgba(251,211,61,0.1);
    border-color: rgba(251,211,61,0.2);
    color: #fbd38d;
}
.tag-red {
    background: rgba(252,129,74,0.1);
    border-color: rgba(252,129,74,0.2);
    color: #fc8181;
}
.tag-purple {
    background: rgba(159,122,234,0.1);
    border-color: rgba(159,122,234,0.2);
    color: #b794f4;
}

/* Map button */
.map-btn {
    display: inline-block;
    background: linear-gradient(135deg, #00d4ff, #0099cc);
    color: #0a0a0f !important;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
    font-size: 0.8rem;
    letter-spacing: 1px;
    padding: 0.5rem 1.5rem;
    border-radius: 8px;
    text-decoration: none;
    margin: 0.3rem;
}

/* Input */
.stTextInput > div > div > input {
    background: #1a1f2e !important;
    border: 1px solid rgba(0,212,255,0.3) !important;
    border-radius: 10px !important;
    color: #e2e8f0 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.95rem !important;
    caret-color: #00d4ff !important;
}
.stTextInput > div > div > input::placeholder {
    color: #718096 !important;
    opacity: 1 !important;
}
.stTextInput > div > div > input:focus {
    background: #1e2435 !important;
    border-color: rgba(0,212,255,0.7) !important;
    box-shadow: 0 0 0 2px rgba(0,212,255,0.15) !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(135deg, #00d4ff, #0099cc) !important;
    color: #0a0a0f !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 10px !important;
    letter-spacing: 2px !important;
    font-size: 0.85rem !important;
    width: 100% !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #00ffcc, #00d4ff) !important;
}

/* Error */
.error-box {
    background: rgba(255,107,107,0.08);
    border: 1px solid rgba(255,107,107,0.3);
    border-radius: 10px;
    padding: 1rem;
    color: #ff6b6b;
    text-align: center;
}

/* Divider */
hr { border-color: rgba(255,255,255,0.05) !important; }

/* Translation table */
.trans-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.5rem;
}
.trans-item {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 8px;
    padding: 0.5rem 0.7rem;
}
.trans-lang { font-size: 0.6rem; color: #4a5568; letter-spacing: 1px; }
.trans-name { font-size: 0.8rem; color: #a0aec0; }
</style>
""", unsafe_allow_html=True)


# ── Helper Functions ──────────────────────────────────────────

def format_population(pop: int) -> str:
    if pop >= 1_000_000_000:
        return f"{pop/1_000_000_000:.2f} Billion"
    if pop >= 1_000_000:
        return f"{pop/1_000_000:.2f} Million"
    if pop >= 1_000:
        return f"{pop/1_000:.1f} Thousand"
    return str(pop)

def format_area(area: float) -> str:
    return f"{area:,.0f} km²"

def get_country_data(country: str):
    url = f"https://restcountries.com/v3.1/name/{country}"
    try:
        res = requests.get(url, timeout=10)
        data = res.json()
        if isinstance(data, dict) and data.get("status") == 404:
            return None, "Country not found!"
        # Best match — exact name first
        for c in data:
            if c["name"]["common"].lower() == country.lower():
                return c, None
        return data[0], None
    except Exception as e:
        return None, str(e)


# ── UI ────────────────────────────────────────────────────────

st.markdown('<div class="main-title">🌍 COUNTRY EXPLORER</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">COMPLETE WORLD INTELLIGENCE DATABASE</div>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col1:
    country_input = st.text_input("", placeholder="Enter country name... (e.g. Japan, Brazil, Egypt)", label_visibility="collapsed")
with col2:
    search = st.button("EXPLORE")

st.markdown("<hr>", unsafe_allow_html=True)

if search and country_input:
    with st.spinner("Fetching country data..."):
        d, error = get_country_data(country_input.strip())

    if error:
        st.markdown(f'<div class="error-box">❌ {error}</div>', unsafe_allow_html=True)

    else:
        # ── Extract all data ──────────────────────────────────
        name_common   = d["name"]["common"]
        name_official = d["name"]["official"]
        flag_emoji    = d.get("flag", "🏳️")
        flag_png      = d["flags"]["png"]
        flag_alt      = d["flags"].get("alt", "")
        coat_png      = d.get("coatOfArms", {}).get("png", "")

        capital       = ", ".join(d.get("capital", ["N/A"]))
        region        = d.get("region", "N/A")
        subregion     = d.get("subregion", "N/A")
        continent     = ", ".join(d.get("continents", ["N/A"]))
        population    = d.get("population", 0)
        area          = d.get("area", 0)
        landlocked    = d.get("landlocked", False)
        independent   = d.get("independent", False)
        un_member     = d.get("unMember", False)
        status        = d.get("status", "N/A")

        languages     = d.get("languages", {})
        currencies    = d.get("currencies", {})
        timezones     = d.get("timezones", [])
        borders       = d.get("borders", [])
        tld           = ", ".join(d.get("tld", ["N/A"]))
        calling_code  = d.get("idd", {})
        car_side      = d.get("car", {}).get("side", "N/A")
        car_sign      = ", ".join(d.get("car", {}).get("signs", ["N/A"]))
        start_week    = d.get("startOfWeek", "N/A").title()
        latlng        = d.get("latlng", [0, 0])
        capital_latlng = d.get("capitalInfo", {}).get("latlng", [])
        google_maps   = d.get("maps", {}).get("googleMaps", "")
        osm_maps      = d.get("maps", {}).get("openStreetMaps", "")
        fifa          = d.get("fifa", "N/A")
        cca2          = d.get("cca2", "N/A")
        cca3          = d.get("cca3", "N/A")
        gini          = d.get("gini", {})
        postal_format = d.get("postalCode", {}).get("format", "N/A")
        demonym       = d.get("demonyms", {}).get("eng", {}).get("m", "N/A")
        alt_spellings = d.get("altSpellings", [])
        native_names  = d.get("name", {}).get("nativeName", {})
        translations  = d.get("translations", {})

        # Calling code
        idd_root   = calling_code.get("root", "")
        idd_suffix = "".join(calling_code.get("suffixes", []))
        phone_code = f"{idd_root}{idd_suffix}" if idd_root else "N/A"

        # ── HERO SECTION ──────────────────────────────────────
        st.markdown(f"""
        <div class="country-hero">
            <div class="country-flag-emoji">{flag_emoji}</div>
            <div class="country-name-hero">{name_common}</div>
            <div class="country-official">{name_official}</div>
            <br>
            <span class="tag">{'✅ Independent' if independent else '❌ Not Independent'}</span>
            <span class="tag-green">{'🇺🇳 UN Member' if un_member else '❌ Not UN Member'}</span>
            <span class="tag-yellow">{'🔒 Landlocked' if landlocked else '🌊 Has Coastline'}</span>
        </div>
        """, unsafe_allow_html=True)

        # ── FLAG + COAT OF ARMS ───────────────────────────────
        fc1, fc2 = st.columns([2, 1])
        with fc1:
            st.image(flag_png, caption=f"🚩 Flag of {name_common}", use_container_width=True)
            if flag_alt:
                st.markdown(f'<div style="color:#4a5568;font-size:0.7rem;margin-top:0.3rem;">{flag_alt}</div>', unsafe_allow_html=True)
        with fc2:
            if coat_png:
                st.image(coat_png, caption="⚜️ Coat of Arms", use_container_width=True)

        # ── BASIC INFO ────────────────────────────────────────
        st.markdown('<div class="section-header">📌 Basic Information</div>', unsafe_allow_html=True)
        b1, b2, b3 = st.columns(3)

        with b1:
            st.markdown(f'<div class="info-card"><div class="card-label">🏛️ Capital City</div><div class="card-value-large">{capital}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-card"><div class="card-label">🌍 Region</div><div class="card-value">{region}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-card"><div class="card-label">🗺️ Sub Region</div><div class="card-value">{subregion}</div></div>', unsafe_allow_html=True)

        with b2:
            st.markdown(f'<div class="info-card"><div class="card-label">👥 Population</div><div class="card-value-large">{format_population(population)}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-card"><div class="card-label">📐 Area</div><div class="card-value">{format_area(area)}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-card"><div class="card-label">🌐 Continent</div><div class="card-value">{continent}</div></div>', unsafe_allow_html=True)

        with b3:
            st.markdown(f'<div class="info-card"><div class="card-label">🧑 Demonym</div><div class="card-value">{demonym}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-card"><div class="card-label">📅 Week Starts</div><div class="card-value">{start_week}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-card"><div class="card-label">📊 Status</div><div class="card-value">{status.replace("-", " ").title()}</div></div>', unsafe_allow_html=True)

        # ── CODES & IDENTIFIERS ───────────────────────────────
        st.markdown('<div class="section-header">🔢 Codes & Identifiers</div>', unsafe_allow_html=True)
        i1, i2, i3, i4, i5 = st.columns(5)
        i1.markdown(f'<div class="info-card"><div class="card-label">🔤 Alpha-2</div><div class="card-value">{cca2}</div></div>', unsafe_allow_html=True)
        i2.markdown(f'<div class="info-card"><div class="card-label">🔤 Alpha-3</div><div class="card-value">{cca3}</div></div>', unsafe_allow_html=True)
        i3.markdown(f'<div class="info-card"><div class="card-label">📞 Calling</div><div class="card-value">{phone_code}</div></div>', unsafe_allow_html=True)
        i4.markdown(f'<div class="info-card"><div class="card-label">🌐 TLD</div><div class="card-value">{tld}</div></div>', unsafe_allow_html=True)
        i5.markdown(f'<div class="info-card"><div class="card-label">⚽ FIFA</div><div class="card-value">{fifa}</div></div>', unsafe_allow_html=True)

        # ── LANGUAGES ─────────────────────────────────────────
        st.markdown('<div class="section-header">🗣️ Languages</div>', unsafe_allow_html=True)
        lang_html = "".join([f'<span class="tag-purple">{v}</span>' for v in languages.values()])
        st.markdown(f'<div class="info-card">{lang_html}</div>', unsafe_allow_html=True)

        # ── CURRENCIES ────────────────────────────────────────
        st.markdown('<div class="section-header">💰 Currencies</div>', unsafe_allow_html=True)
        cur_cols = st.columns(len(currencies) if currencies else 1)
        for i, (code, info) in enumerate(currencies.items()):
            cur_cols[i].markdown(f'''
            <div class="info-card">
                <div class="card-label">Currency Code</div>
                <div class="card-value-large">{info.get("symbol","?")} {code}</div>
                <div class="card-value">{info.get("name","N/A")}</div>
            </div>''', unsafe_allow_html=True)

        # ── TIMEZONES ─────────────────────────────────────────
        st.markdown('<div class="section-header">🕐 Timezones</div>', unsafe_allow_html=True)
        tz_html = "".join([f'<span class="tag-green">{tz}</span>' for tz in timezones])
        st.markdown(f'<div class="info-card">{tz_html}</div>', unsafe_allow_html=True)

        # ── LOCATION ──────────────────────────────────────────
        st.markdown('<div class="section-header">📍 Location & Geography</div>', unsafe_allow_html=True)
        l1, l2, l3 = st.columns(3)
        l1.markdown(f'<div class="info-card"><div class="card-label">📍 Coordinates</div><div class="card-value">{latlng[0]}°, {latlng[1]}°</div></div>', unsafe_allow_html=True)
        l2.markdown(f'<div class="info-card"><div class="card-label">🏙️ Capital Coords</div><div class="card-value">{capital_latlng[0] if capital_latlng else "N/A"}°, {capital_latlng[1] if capital_latlng else "N/A"}°</div></div>', unsafe_allow_html=True)
        l3.markdown(f'<div class="info-card"><div class="card-label">🚗 Drive Side</div><div class="card-value">{"🛞 Left Side" if car_side=="left" else "🛞 Right Side"}</div><div style="color:#718096;font-size:0.7rem;">Sign: {car_sign}</div></div>', unsafe_allow_html=True)

        # Borders
        if borders:
            borders_html = "".join([f'<span class="tag-red">{b}</span>' for b in borders])
            st.markdown(f'<div class="info-card"><div class="card-label">🗺️ Bordering Countries ({len(borders)})</div><div style="margin-top:0.4rem">{borders_html}</div></div>', unsafe_allow_html=True)

        # Maps
        map_html = ""
        if google_maps:
            map_html += f'<a href="{google_maps}" target="_blank" class="map-btn">🗺️ Google Maps</a>'
        if osm_maps:
            map_html += f'<a href="{osm_maps}" target="_blank" class="map-btn">🌐 OpenStreetMap</a>'
        if map_html:
            st.markdown(f'<div class="info-card"><div class="card-label">🔗 View on Map</div><div style="margin-top:0.5rem">{map_html}</div></div>', unsafe_allow_html=True)

        # ── EXTRA INFO ────────────────────────────────────────
        st.markdown('<div class="section-header">📋 Additional Info</div>', unsafe_allow_html=True)
        e1, e2 = st.columns(2)

        with e1:
            if gini:
                year, val = list(gini.items())[-1]
                st.markdown(f'<div class="info-card"><div class="card-label">📊 Gini Coefficient ({year})</div><div class="card-value">{val} <span style="color:#718096;font-size:0.75rem;">(Income Inequality Index)</span></div></div>', unsafe_allow_html=True)
            if postal_format and postal_format != "None":
                st.markdown(f'<div class="info-card"><div class="card-label">📮 Postal Code Format</div><div class="card-value">{postal_format}</div></div>', unsafe_allow_html=True)

        with e2:
            if alt_spellings:
                alt_html = "".join([f'<span class="tag">{s}</span>' for s in alt_spellings[:6]])
                st.markdown(f'<div class="info-card"><div class="card-label">🔤 Also Known As</div><div style="margin-top:0.4rem">{alt_html}</div></div>', unsafe_allow_html=True)

        # Native Names
        if native_names:
            native_html = "".join([f'<span class="tag-yellow">{v["common"]}</span>' for v in native_names.values()])
            st.markdown(f'<div class="info-card"><div class="card-label">🗣️ Native Names</div><div style="margin-top:0.4rem">{native_html}</div></div>', unsafe_allow_html=True)

        # ── TRANSLATIONS ──────────────────────────────────────
        if translations:
            st.markdown('<div class="section-header">🌐 Name in Other Languages</div>', unsafe_allow_html=True)
            lang_map = {
                "ara":"Arabic","bre":"Breton","ces":"Czech","deu":"German",
                "est":"Estonian","fin":"Finnish","fra":"French","hrv":"Croatian",
                "hun":"Hungarian","ind":"Indonesian","ita":"Italian","jpn":"Japanese",
                "kor":"Korean","nld":"Dutch","per":"Persian","pol":"Polish",
                "por":"Portuguese","rus":"Russian","spa":"Spanish","srp":"Serbian",
                "swe":"Swedish","tur":"Turkish","urd":"Urdu","zho":"Chinese"
            }
            trans_html = '<div class="trans-grid">'
            for code, val in list(translations.items())[:18]:
                lang_name = lang_map.get(code, code.upper())
                trans_html += f'<div class="trans-item"><div class="trans-lang">{lang_name}</div><div class="trans-name">{val["common"]}</div></div>'
            trans_html += '</div>'
            st.markdown(trans_html, unsafe_allow_html=True)

        # ── FOOTER ────────────────────────────────────────────
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown(f'<div style="text-align:center;color:#2d3748;font-size:0.7rem;letter-spacing:2px;">◈ DATA FROM RESTCOUNTRIES.COM ◈ NO API KEY NEEDED ◈</div>', unsafe_allow_html=True)

elif search and not country_input:
    st.markdown('<div class="error-box">⚠️ Please enter a country name</div>', unsafe_allow_html=True)

else:
    st.markdown("""
    <div style="text-align:center;color:#2d3748;padding:4rem 0;">
        <div style="font-size:4rem;margin-bottom:1rem;">🌍</div>
        <div style="font-size:0.85rem;letter-spacing:3px;margin-bottom:0.5rem;">EXPLORE ANY COUNTRY</div>
        <div style="font-size:0.7rem;letter-spacing:1px;color:#1a202c;">Population • Capital • Languages • Currency • Timezones • Borders • Maps & More</div>
    </div>
    """, unsafe_allow_html=True)
