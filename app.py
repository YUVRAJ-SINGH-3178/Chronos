import streamlit as st
import datetime
import time
import random
import base64
import uuid # For UUID generation
import streamlit.components.v1 as components

# --- Configuration and Constants ---
ACCENT_CYAN = "#00FFFF"
ACCENT_MAGENTA = "#FF00FF"
ACCENT_GREEN = "#00FF80"
TEXT_BASE = "#E8F0F5"
TEXT_SUBTLE = "#8A9BA8"

# Function to load and apply custom CSS using st.markdown (most reliable for global styles)
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Page Configuration (Must be the very first Streamlit command) ---
st.set_page_config(
    page_title="Chronos: Universal Converter",
    page_icon="🕰️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Apply our custom CSS immediately after page config ---
load_css("style.css")

# --- TOP ABOUT/CREDITS BANNER ---
st.markdown(f"""
    <div class="about-banner-container">
        <p class="about-text">
            DEVELOPED BY <span style="color:{ACCENT_CYAN}; text-shadow: 0 0 8px {ACCENT_CYAN};">YUVRAJ SINGH</span>
        </p>
        <p class="about-text">
            GITHUB: <a href="https://github.com/YUVRAJ-SINGH-3178" target="_blank" style="color:{ACCENT_MAGENTA}; text-shadow: 0 0 8px {ACCENT_MAGENTA}; text-decoration: none;">YUVRAJ-SINGH-3178</a>
        </p>
    </div>
    """, unsafe_allow_html=True)


# --- Main App Content Header ---
st.markdown(f"""
    <div class="header-container">
        <h1 class="main-title">CHRONOS</h1>
        <p class="subtitle blink-text">:: UNIVERSAL DATA TERMINAL ::</p>
        <div class="scanline"></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='separator'>", unsafe_allow_html=True)


# --- Sidebar for Navigation/Features ---
with st.sidebar:
    st.markdown(f"<h1 class='main-title' style='font-size: 2.2em; text-shadow: {ACCENT_MAGENTA} 0 0 15px; color: {ACCENT_MAGENTA};'>CHRONOS NAV</h1>", unsafe_allow_html=True)
    st.markdown("<hr class='separator' style='margin: 1.5rem 0; border-top: 2px solid rgba(255,0,255,0.2);'>", unsafe_allow_html=True)

    selected_feature = st.radio(
        "SELECT MODULE:",
        ("Time Translator", "Text Utility", "Data Decryptor", "Inter-Unit Converter", "Random Data Generator", "System Monitor", "Settings"), # Hashing removed
        key="sidebar_radio"
    )
    st.markdown("<hr class='separator' style='margin: 1.5rem 0; border-top: 2px solid rgba(255,0,255,0.2);'>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div style='text-align: center; margin-top: 2.5rem;'>
            <span style='font-family: var(--font-mono); font-size: 1em; color: {TEXT_SUBTLE};'>
                SYSTEM STATUS: <span style='color: {ACCENT_GREEN}; text-shadow: 0 0 8px {ACCENT_GREEN};'>ONLINE</span>
            </span>
        </div>
        """, unsafe_allow_html=True
    )


# --- Module Content Display ---
if selected_feature == "Time Translator":
    st.markdown("<div class='module-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='module-title'>UNIVERSAL TIME TRANSLATOR</h2>", unsafe_allow_html=True)

    current_datetime = datetime.datetime.now()

    st.markdown(f"""
        <div class="time-display-grid">
            <div>
                <span class="time-label">LOCAL UTC OFFSET:</span>
                <p class="digital-value">{current_datetime.strftime("%Y-%m-%d %H:%M:%S %Z%z")}</p>
            </div>
            <div>
                <span class="time-label">UNIX TIMESTAMP (EPOCH):</span>
                <p class="digital-value">{int(current_datetime.timestamp())}</p>
            </div>
            <div>
                <span class="time-label">ISO 8601 FORMAT:</span>
                <p class="digital-value">{current_datetime.isoformat(timespec='seconds')}</p>
            </div>
            <div>
                <span class="time-label">JULIAN DATE (JD):</span>
                <p class="digital-value">{current_datetime.toordinal() + 1721425.5:.4f}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    if st.button("SYNCHRONIZE TEMPORAL FLUX", key="sync_time_btn"):
        with st.spinner('Calibrating temporal flux...'):
            time.sleep(1.5)
        st.toast("Temporal synchronization complete. All Chronos modules calibrated.")
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_feature == "Text Utility":
    st.markdown("<div class='module-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='module-title'>TEXT MANIPULATION UNIT</h2>", unsafe_allow_html=True)

    text_input = st.text_area("ENTER TEXT FOR PROCESSING:", key="text_utility_input", height=200)

    if 'text_output_util' not in st.session_state:
        st.session_state.text_output_util = ""

    st.markdown("<hr style='border-top: 1px dashed rgba(0, 255, 255, 0.2); margin: 2rem 0;'>", unsafe_allow_html=True)

    col_text_ops_1, col_text_ops_2 = st.columns(2)

    with col_text_ops_1:
        st.subheader("CASE CONVERSION")
        if st.button("TO UPPERCASE", key="to_upper"):
            st.session_state.text_output_util = text_input.upper()
        if st.button("to lowercase", key="to_lower"):
            st.session_state.text_output_util = text_input.lower()
        if st.button("Title Case", key="to_title"):
            st.session_state.text_output_util = text_input.title()
        if st.button("Sentence case", key="to_sentence"):
            if text_input:
                sentences = text_input.split('.')
                processed_sentences = [s.strip().capitalize() for s in sentences if s.strip()]
                st.session_state.text_output_util = ". ".join(processed_sentences) + ("." if text_input.endswith('.') else "")
            else:
                st.session_state.text_output_util = ""

    with col_text_ops_2:
        st.subheader("TEXT CLEANING & ORGANIZE")
        if st.button("TRIM WHITESPACE", key="trim_ws"):
            st.session_state.text_output_util = " ".join(text_input.split())
        if st.button("REMOVE DUPLICATE LINES", key="remove_dup_lines"):
            lines = text_input.splitlines()
            unique_lines = []
            seen = set()
            for line in lines:
                if line not in seen:
                    unique_lines.append(line)
                    seen.add(line)
            st.session_state.text_output_util = "\n".join(unique_lines)
        sort_option = st.radio("SORT LINES:", ("None", "Ascending (A-Z)", "Descending (Z-A)"), key="sort_lines_radio")
        if sort_option == "Ascending (A-Z)":
            lines = text_input.splitlines()
            st.session_state.text_output_util = "\n".join(sorted(lines))
        elif sort_option == "Descending (Z-A)":
            lines = text_input.splitlines()
            st.session_state.text_output_util = "\n".join(sorted(lines, reverse=True))

    st.markdown("<hr style='border-top: 1px dashed rgba(0, 255, 255, 0.2); margin: 2rem 0;'>", unsafe_allow_html=True)
    st.subheader("TEXT METRICS")
    if text_input:
        words = len(text_input.split())
        chars = len(text_input)
        lines = text_input.count('\n') + 1 if text_input else 0
        st.markdown(f"<p style='font-family: var(--font-mono); color: var(--text-base);'>Words: <strong>{words}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-family: var(--font-mono); color: var(--text-base);'>Characters: <strong>{chars}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-family: var(--font-mono); color: var(--text-base);'>Lines: <strong>{lines}</strong></p>", unsafe_allow_html=True)
    else:
        st.info("Enter text to see metrics.")

    # Display output
    if st.session_state.text_output_util:
        st.markdown(f"""
            <div class="result-display-wrapper">
                <span class="result-label">PROCESSED TEXT:</span>
                <p class="digital-value result-value" style="font-size: 1.5em; word-break: break-all;">
                    {st.session_state.text_output_util}
                </p>
            </div>
        """, unsafe_allow_html=True)
    else:
         st.markdown(f"""
            <div class="result-display-wrapper">
                <span class="result-label">OUTPUT:</span>
                <p class="digital-value result-value placeholder" style="font-size: 1.5em;">
                    READY
                </p>
            </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_feature == "Data Decryptor":
    st.markdown("<div class='module-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='module-title'>DATA DECRYPTOR / ENCRYPTOR</h2>", unsafe_allow_html=True)

    data_input = st.text_area("ENTER DATA STRING FOR PROCESSING:", key="data_decryptor_input", height=200)

    if 'data_output_decryptor' not in st.session_state:
        st.session_state.data_output_decryptor = ""

    st.markdown("<hr style='border-top: 1px dashed rgba(0, 255, 255, 0.2); margin: 2rem 0;'>", unsafe_allow_html=True)

    # Using a single column for the buttons to ensure they stack and align well
    col_b64_ops = st.columns(1)

    with col_b64_ops[0]:
        if st.button("ENCODE TO BASE64", key="encode_b64_new"):
            if data_input:
                try:
                    encoded = base64.b64encode(data_input.encode('utf-8')).decode('utf-8')
                    st.session_state.data_output_decryptor = encoded
                except Exception as e:
                    st.error(f"Encoding error: {e}")
            else:
                st.warning("Enter data to encode.")
        if st.button("DECODE FROM BASE64", key="decode_b64_new"):
            if data_input:
                try:
                    decoded = base64.b64decode(data_input.encode('utf-8')).decode('utf-8')
                    st.session_state.data_output_decryptor = decoded
                except Exception as e:
                    st.error(f"Decoding error: {e} (Is it valid Base64?)")
            else:
                st.warning("Enter Base64 string to decode.")

    st.markdown("<hr style='border-top: 1px dashed rgba(0, 255, 255, 0.2); margin: 2rem 0;'>", unsafe_allow_html=True)

    # Display output
    if st.session_state.data_output_decryptor:
        st.markdown(f"""
            <div class="result-display-wrapper">
                <span class="result-label">PROCESSED DATA:</span>
                <p class="digital-value result-value" style="font-size: 1.5em; word-break: break-all;">
                    {st.session_state.data_output_decryptor}
                </p>
            </div>
        """, unsafe_allow_html=True)
    else:
         st.markdown(f"""
            <div class="result-display-wrapper">
                <span class="result-label">OUTPUT:</span>
                <p class="digital-value result-value placeholder" style="font-size: 1.5em;">
                    READY
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

elif selected_feature == "Inter-Unit Converter":
    st.markdown("<div class='module-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='module-title'>INTER-UNIT CONVERTER</h2>", unsafe_allow_html=True)

    st.markdown("<hr style='border-top: 1px dashed rgba(0, 255, 255, 0.2); margin: 2rem 0;'>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1]) # Use columns for alignment

    with col1:
        st.write("### CONVERT FROM:")
        convert_from_value = st.number_input("Value", value=1.0, key="convert_from_val")
        convert_from_unit_category = st.selectbox(
            "Unit Category",
            ("Length", "Mass", "Time", "Temperature"),
            key="convert_from_unit_category"
        )
        # Dynamic unit selection based on category
        if convert_from_unit_category == "Length":
            st.selectbox("Select Length Unit:", ("Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"), key="length_from_unit")
        elif convert_from_unit_category == "Mass":
            st.selectbox("Select Mass Unit:", ("Kilogram", "Gram", "Milligram", "Pound", "Ounce"), key="mass_from_unit")
        elif convert_from_unit_category == "Time":
            st.selectbox("Select Time Unit:", ("Second", "Minute", "Hour", "Day"), key="time_from_unit")
        elif convert_from_unit_category == "Temperature":
            st.selectbox("Select Temperature Unit:", ("Celsius", "Fahrenheit", "Kelvin"), key="temp_from_unit")

    with col2:
        st.write("### CONVERSION TYPE:")
        conversion_type_display = st.selectbox(
            "Conversion Category:",
            ("Length", "Mass", "Time", "Temperature"), # Only show relevant categories
            key="conversion_category_display"
        )
        st.markdown("<br><br><br>", unsafe_allow_html=True) # Placeholder for vertical spacing
        if st.button("EXECUTE CONVERSION", key="execute_conversion_btn"):
            st.info("Conversion logic to be implemented here!") # Placeholder for logic

    with col3:
        st.write("### CONVERT TO:")
        convert_to_unit_category = st.selectbox(
            "Unit Category",
            ("Length", "Mass", "Time", "Temperature"),
            key="convert_to_unit_category"
        )
        # Dynamic unit selection based on category
        if convert_to_unit_category == "Length":
            st.selectbox("Select Length Unit:", ("Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"), key="length_to_unit")
        elif convert_to_unit_category == "Mass":
            st.selectbox("Select Mass Unit:", ("Kilogram", "Gram", "Milligram", "Pound", "Ounce"), key="mass_to_unit")
        elif convert_to_unit_category == "Time":
            st.selectbox("Select Time Unit:", ("Second", "Minute", "Hour", "Day"), key="time_to_unit")
        elif convert_to_unit_category == "Temperature":
            st.selectbox("Select Temperature Unit:", ("Celsius", "Fahrenheit", "Kelvin"), key="temp_to_unit")


    st.markdown("<hr style='border-top: 1px dashed rgba(0, 255, 255, 0.2); margin: 2rem 0;'>", unsafe_allow_html=True)

    st.markdown(f"""
        <div class="result-display-wrapper">
            <span class="result-label">CONVERTED VALUE:</span>
            <p class="digital-value result-value placeholder" style="font-size: 1.5em;">
                RESULT HERE
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

elif selected_feature == "Random Data Generator":
    st.markdown("<div class='module-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='module-title'>RANDOM DATA GENERATOR</h2>", unsafe_allow_html=True)

    st.markdown("<hr style='border-top: 1px dashed rgba(0, 255, 255, 0.2); margin: 2rem 0;'>", unsafe_allow_html=True)

    generator_type = st.radio(
        "SELECT DATA TYPE:",
        ("Random Integer", "Random Float", "Random String (Alphanumeric)", "UUID", "Random Hex Color"),
        key="generator_type_radio"
    )

    if 'generated_data_output' not in st.session_state:
        st.session_state.generated_data_output = "READY"

    if generator_type == "Random Integer":
        col_int_min, col_int_max = st.columns(2)
        with col_int_min:
            min_val = st.number_input("Minimum Value:", value=0, step=1, key="int_min")
        with col_int_max:
            max_val = st.number_input("Maximum Value:", value=100, step=1, key="int_max")
        if st.button("GENERATE INTEGER", key="generate_int_btn"):
            if min_val <= max_val:
                st.session_state.generated_data_output = str(random.randint(min_val, max_val))
            else:
                st.error("Min value cannot be greater than Max value.")

    elif generator_type == "Random Float":
        col_float_min, col_float_max = st.columns(2)
        with col_float_min:
            min_float = st.number_input("Minimum Value:", value=0.0, key="float_min")
        with col_float_max:
            max_float = st.number_input("Maximum Value:", value=1.0, key="float_max")
        decimal_places = st.slider("Decimal Places:", min_value=0, max_value=10, value=4, key="float_dp")
        if st.button("GENERATE FLOAT", key="generate_float_btn"):
            if min_float <= max_float:
                rand_float = random.uniform(min_float, max_float)
                st.session_state.generated_data_output = f"{rand_float:.{decimal_places}f}"
            else:
                st.error("Min value cannot be greater than Max value.")

    elif generator_type == "Random String (Alphanumeric)":
        string_length = st.slider("String Length:", min_value=1, max_value=100, value=16, key="string_len")
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        if st.button("GENERATE STRING", key="generate_string_btn"):
            st.session_state.generated_data_output = ''.join(random.choice(chars) for _ in range(string_length))

    elif generator_type == "UUID":
        st.markdown("<p style='font-family: var(--font-mono); color: var(--text-subtle);'>Generates a universally unique identifier (UUID v4).</p>", unsafe_allow_html=True)
        if st.button("GENERATE UUID", key="generate_uuid_btn"):
            st.session_state.generated_data_output = str(uuid.uuid4())

    elif generator_type == "Random Hex Color":
        st.markdown("<p style='font-family: var(--font-mono); color: var(--text-subtle);'>Generates a random hexadecimal color code (e.g., #RRGGBB).</p>", unsafe_allow_html=True)
        if st.button("GENERATE COLOR", key="generate_color_btn"):
            st.session_state.generated_data_output = '#%06x' % random.randint(0, 0xFFFFFF)


    st.markdown("<hr style='border-top: 1px dashed rgba(0, 255, 255, 0.2); margin: 2rem 0;'>", unsafe_allow_html=True)

    # Display output
    st.markdown(f"""
        <div class="result-display-wrapper">
            <span class="result-label">GENERATED DATA:</span>
            <p class="digital-value result-value" style="font-size: 1.5em; word-break: break-all;">
                {st.session_state.generated_data_output}
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


elif selected_feature == "System Monitor":
    st.markdown("<div class='module-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='module-title'>SYSTEM STATUS OVERVIEW</h2>", unsafe_allow_html=True)

    cpu_load = random.randint(15, 95)
    memory_usage = random.randint(20, 85)
    network_latency = round(random.uniform(5, 150), 2)
    server_temp = round(random.uniform(30, 70), 1)

    def get_status_color(value, threshold_warn, threshold_crit, accent_base):
        if value >= threshold_crit: return "#FF3860" # Red for critical
        elif value >= threshold_warn: return ACCENT_GREEN # Use green for warning (fits scheme)
        else: return accent_base

    cpu_color = get_status_color(cpu_load, 70, 90, ACCENT_CYAN)
    mem_color = get_status_color(memory_usage, 60, 80, ACCENT_MAGENTA)
    latency_color = get_status_color(network_latency, 80, 120, ACCENT_CYAN)
    temp_color = get_status_color(server_temp, 50, 65, ACCENT_MAGENTA)

    st.markdown(f"""
        <div class="status-grid">
            <div class="status-item">
                <span class="status-label">CPU LOAD:</span>
                <div class="progress-bar-container">
                    <div class="progress-bar" style="width: {cpu_load}%; background-color: {cpu_color}; box-shadow: 0 0 18px {cpu_color};"></div>
                </div>
                <span class="status-value" style="color: {cpu_color}; text-shadow: var(--glow-strong) {cpu_color};">{cpu_load}%</span>
            </div>
            <div class="status-item">
                <span class="status-label">MEMORY USAGE:</span>
                <div class="progress-bar-container">
                    <div class="progress-bar" style="width: {memory_usage}%; background-color: {mem_color}; box-shadow: 0 0 18px {mem_color};"></div>
                </div>
                <span class="status-value" style="color: {mem_color}; text-shadow: var(--glow-strong) {mem_color};">{memory_usage}%</span>
            </div>
            <div class="status-item">
                <span class="status-label">NETWORK LATENCY:</span>
                <p class="digital-value" style="color: {latency_color}; text-shadow: var(--glow-strong) {latency_color};">{network_latency} ms</p>
            </div>
            <div class="status-item">
                <span class="status-label">SERVER TEMP:</span>
                <p class="digital-value" style="color: {temp_color}; text-shadow: var(--glow-strong) {temp_color};">{server_temp}°C</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    if st.button("RUN DIAGNOSTIC SCAN", key="diagnostic_scan_btn"):
        with st.spinner('Initiating system diagnostics...'):
            time.sleep(2)
        st.toast("Diagnostic scan complete. Anomalies detected: None.")

    st.markdown("</div>", unsafe_allow_html=True)


elif selected_feature == "Settings":
    st.markdown("<div class='module-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='module-title'>SYSTEM SETTINGS</h2>", unsafe_allow_html=True)

    st.write("Configure Chronos module parameters and display options.")

    st.subheader("DISPLAY OPTIONS")
    st.checkbox("ENABLE HEADER GLITCH EFFECT", value=True, help="Toggle the animated text glitch on the main title.", key="glitch_toggle")
    st.checkbox("ENABLE BACKGROUND GRID", value=True, help="Toggle the subtle grid overlay in the background.", key="grid_toggle")

    st.info("Advanced theme customization (e.g., custom color pickers directly affecting CSS variables) requires more complex Streamlit components or JavaScript, which is beyond basic Streamlit. For now, enjoy the pre-configured cyberpunk theme!")

    st.subheader("DATA MANAGEMENT")
    if st.button("PURGE ALL TEMPORARY DATA CACHE", key="purge_cache_btn"):
        with st.spinner('Initiating full cache purge...'):
            time.sleep(1.5)
        st.success("All temporary data cache purged. System optimized and secured.")

    st.markdown(f"<br><p style='font-family: var(--font-mono); color: {TEXT_SUBTLE}; font-size: 0.9em; text-align: center;'>Chronos Protocol Version 1.0.2 | <span style='color: {ACCENT_GREEN}; text-shadow: 0 0 5px {ACCENT_GREEN};'>ACTIVE</span></p>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# --- Final JavaScript for extremely stubborn cases (e.g., ensuring selectbox text color) ---
# This JavaScript is designed to run after Streamlit's rendering and specifically target
# the selected text in selectboxes to ensure it's readable.
# This is a defensive measure and should run even if CSS covers most cases.
js_fix_code = f"""
<script>
    function applySelectboxFix() {{
        // Target for the displayed selected value in the closed selectbox (the visible text)
        // Using more specific, common Streamlit emotion-cache classes for v1.47.1
        // These are the classes BaseWeb/Streamlit uses for the *displayed value*
        const targetSpanSelector = '.stSelectbox .st-emotion-cache-1f871x7 span, .stSelectbox .st-emotion-cache-1by3y0f span, .st-emotion-cache-j9p1l6';
        const targetDivSelector = '.stSelectbox .st-emotion-cache-1f871x7, .stSelectbox .st-emotion-cache-1by3y0f, .st-emotion-cache-p2w2j5';

        // Target for the currently selected item in the *open* dropdown list
        const dropdownListItemSelector = 'div[data-baseweb="popover"] ul li[aria-selected="true"]';
        // Target for ALL items in the open dropdown list (to set default color)
        const dropdownAllItemsSelector = 'div[data-baseweb="popover"] ul li';


        // Apply styles to the displayed selected value in the closed selectbox
        document.querySelectorAll(targetSpanSelector).forEach(span => {{
            span.style.setProperty('color', '{ACCENT_CYAN}', 'important');
            span.style.setProperty('background-color', 'transparent', 'important');
            span.style.setProperty('text-shadow', '0 0 10px {ACCENT_CYAN}', 'important');
            span.style.setProperty('font-weight', 'bold', 'important');
            span.style.setProperty('padding-top', '2px', 'important');
            span.style.setProperty('padding-bottom', '2px', 'important');
            span.style.setProperty('display', 'block', 'important'); // Critical for vertical padding/alignment
            span.style.setProperty('line-height', '1.2', 'important');
            span.style.setProperty('font-family', 'var(--font-mono)', 'important');
            span.style.setProperty('font-size', '1.3em', 'important');
        }});

        // Apply styles to the parent div of the displayed selected value
        document.querySelectorAll(targetDivSelector).forEach(div => {{
            div.style.setProperty('color', '{ACCENT_CYAN}', 'important'); // Fallback
            div.style.setProperty('background-color', 'transparent', 'important'); // Ensure no background
            div.style.setProperty('font-family', 'var(--font-mono)', 'important');
            div.style.setProperty('font-size', '1.3em', 'important');
            div.style.setProperty('padding', '0 !important', 'important'); // Reset padding more aggressively
            div.style.setProperty('align-items', 'center', 'important'); // Ensure vertical alignment
            div.style.setProperty('display', 'flex', 'important'); // Ensure flex behavior
        }});

        // Apply styles to the currently selected item in the *open* dropdown list
        document.querySelectorAll(dropdownListItemSelector).forEach(item => {{
            item.style.setProperty('background-color', 'rgba(255, 0, 255, 0.5)', 'important'); /* Magenta highlight */
            item.style.setProperty('color', '{ACCENT_CYAN}', 'important'); /* Cyan text */
            item.style.setProperty('text-shadow', '0 0 8px {ACCENT_CYAN}', 'important');
            item.style.setProperty('font-weight', 'bold', 'important');
        }});

        // Ensure all other items in the dropdown list are readable
        document.querySelectorAll(dropdownAllItemsSelector).forEach(item => {{
            item.style.setProperty('color', '{TEXT_BASE}', 'important'); // Base text color for unselected
            item.style.setProperty('font-family', 'var(--font-mono)', 'important');
        }});
    }}

    // Use MutationObserver for continuous application due to Streamlit's dynamic DOM updates
    const observer = new MutationObserver((mutationsList, observer) => {{
        let shouldApplyFix = false;
        for (const mutation of mutationsList) {{
            if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {{
                // Check if any added node is a selectbox or part of its dropdown popover
                mutation.addedNodes.forEach(node => {{
                    if (node.nodeType === 1) {{ // Only element nodes
                        if (node.matches('.stSelectbox') || node.querySelector('.stSelectbox')) {{
                            shouldApplyFix = true;
                        }}
                        if (node.matches('div[data-baseweb="popover"]') || node.querySelector('div[data-baseweb="popover"]')) {{
                            shouldApplyFix = true;
                        }}
                        // Specific Streamlit emotion-cache classes that are common targets
                        if (node.matches('.st-emotion-cache-1f871x7') || node.matches('.st-emotion-cache-1by3y0f') ||
                            node.matches('.st-emotion-cache-j9p1l6') || node.matches('.st-emotion-cache-p2w2j5')) {{
                            shouldApplyFix = true;
                        }}
                    }}
                }});
            }} else if (mutation.type === 'attributes' && mutation.attributeName === 'aria-selected') {{
                // When a selectbox item is selected, its 'aria-selected' attribute changes
                if (mutation.target.matches('li[aria-selected="true"]')) {{
                    shouldApplyFix = true;
                }}
            }}
        }}
        if (shouldApplyFix) {{
            // Add a small delay to ensure Streamlit's own rendering completes before applying our fix
            setTimeout(applySelectboxFix, 50);
        }}
    }});

    // Observe the entire document body for changes
    observer.observe(document.body, {{ childList: true, subtree: true, attributes: true }});

    // Run once initially on page load, with a slight delay
    setTimeout(applySelectboxFix, 150); // Slightly longer initial delay
</script>
"""
components.html(js_fix_code, height=0, width=0)