import streamlit as st

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="GlowCare AI",
    page_icon="🌸",
    layout="wide"
)

# ---------------- CUSTOM DESIGN ----------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #fff5f8, #f4f0ff);
}

.main-title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    color: #9b4d7b;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #6d5a66;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 20px;
    margin: 15px 0px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
}

.section-title {
    color: #9b4d7b;
    font-size: 30px;
    font-weight: bold;
}

.product {
    background-color: #fffafd;
    padding: 15px;
    border-radius: 15px;
    margin: 10px 0px;
    border: 1px solid #f0dce7;
}

.warning {
    background-color: #fff4d6;
    padding: 15px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------

st.sidebar.title("🌸 GlowCare AI")

page = st.sidebar.selectbox(
    "Choose a section",
    [
        "🏠 Home",
        "📸 AI Skin Analysis",
        "🧴 Product Recommendations",
        "☀️ Sunscreen Guide",
        "🌙 Skincare Routine",
        "⚠️ Safety Information"
    ]
)


# =====================================================
# HOME PAGE
# =====================================================

if page == "🏠 Home":

    st.markdown(
        '<div class="main-title">🌸 GlowCare AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Your Personal AI Skincare Assistant ✨</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown("""
    <div class="card">

    ### ✨ Welcome to GlowCare AI

    Take a photo, tell us about your skin, and explore
    personalized skincare suggestions.

    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h2>📸</h2>
        <h3>Skin Analysis</h3>
        <p>Capture a face photo and record visible skin concerns.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h2>🧴</h2>
        <h3>Product Guide</h3>
        <p>Explore cleanser, moisturizer, serum and sunscreen categories.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h2>🌙</h2>
        <h3>Daily Routine</h3>
        <p>Create a simple morning and night skincare routine.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info(
        "🌿 This application provides general skincare information. "
        "It does not diagnose skin diseases."
    )


# =====================================================
# AI SKIN ANALYSIS
# =====================================================

elif page == "📸 AI Skin Analysis":

    st.markdown(
        '<div class="section-title">📸 AI Skin Analysis</div>',
        unsafe_allow_html=True
    )

    st.write("Take a clear photo in good lighting.")

    picture = st.camera_input("📷 Take your photo")

    if picture is not None:

        st.success("Photo captured successfully! ✅")

        st.image(
            picture,
            caption="Skin Analysis Photo",
            use_container_width=True
        )

        st.divider()

        st.subheader("🧴 Select your skin type")

        skin_type = st.selectbox(
            "Skin Type",
            [
                "Oily",
                "Dry",
                "Combination",
                "Normal",
                "Sensitive",
                "I don't know"
            ]
        )

        st.subheader("🔍 Select visible concerns")

        col1, col2 = st.columns(2)

        with col1:

            acne = st.checkbox("🔴 Acne / Pimples")
            blackheads = st.checkbox("⚫ Blackheads")
            whiteheads = st.checkbox("⚪ Whiteheads")
            pores = st.checkbox("🕳️ Visible Pores")
            excess_oil = st.checkbox("💧 Excess Oil")
            dryness = st.checkbox("🏜️ Dryness")

        with col2:

            redness = st.checkbox("🔴 Redness")
            tan = st.checkbox("☀️ Tan / Uneven Tone")
            dark_spots = st.checkbox("🟤 Dark Spots")
            dark_circles = st.checkbox("👁️ Dark Circles")
            irritation = st.checkbox("⚠️ Irritation")
            uneven_texture = st.checkbox("〰️ Uneven Texture")

        if st.button("✨ Generate Skincare Suggestions"):

            st.success("Your skincare suggestions are ready! 🌸")

            st.header("📋 Your Skin Profile")

            st.write(f"**Selected skin type:** {skin_type}")

            # ---------------- OILY ----------------

            if skin_type == "Oily":

                st.subheader("💧 For Oily Skin")

                st.markdown("""
                <div class="product">

                <b>Face Wash</b><br>
                Look for a gentle foaming cleanser.

                <br><br>

                <b>Moisturizer</b><br>
                Choose a lightweight, non-comedogenic moisturizer.

                <br><br>

                <b>Serum</b><br>
                Niacinamide can be considered for oil control.

                </div>
                """, unsafe_allow_html=True)

            # ---------------- DRY ----------------

            elif skin_type == "Dry":

                st.subheader("🏜️ For Dry Skin")

                st.markdown("""
                <div class="product">

                <b>Face Wash</b><br>
                Choose a gentle, fragrance-free hydrating cleanser.

                <br><br>

                <b>Moisturizer</b><br>
                Choose a cream-based moisturizer.

                <br><br>

                <b>Serum</b><br>
                Hydrating ingredients such as hyaluronic acid can be considered.

                </div>
                """, unsafe_allow_html=True)

            # ---------------- COMBINATION ----------------

            elif skin_type == "Combination":

                st.subheader("🌸 For Combination Skin")

                st.markdown("""
                <div class="product">

                <b>Face Wash</b><br>
                Gentle cleanser.

                <br><br>

                <b>Moisturizer</b><br>
                Lightweight non-comedogenic moisturizer.

                <br><br>

                <b>Serum</b><br>
                A simple hydrating or niacinamide serum may be considered.

                </div>
                """, unsafe_allow_html=True)

            # ---------------- NORMAL ----------------

            elif skin_type == "Normal":

                st.subheader("🌷 For Normal Skin")

                st.markdown("""
                <div class="product">

                <b>Face Wash</b><br>
                Gentle cleanser.

                <br><br>

                <b>Moisturizer</b><br>
                Lightweight moisturizer.

                <br><br>

                <b>Serum</b><br>
                Hydrating serum if needed.

                </div>
                """, unsafe_allow_html=True)

            # ---------------- SENSITIVE ----------------

            elif skin_type == "Sensitive":

                st.subheader("🌿 For Sensitive Skin")

                st.markdown("""
                <div class="product">

                <b>Face Wash</b><br>
                Gentle fragrance-free cleanser.

                <br><br>

                <b>Moisturizer</b><br>
                Fragrance-free moisturizer.

                <br><br>

                <b>Serum</b><br>
                Keep the routine simple and avoid introducing many
                active ingredients at once.

                </div>
                """, unsafe_allow_html=True)

            # ---------------- UNKNOWN ----------------

            else:

                st.info(
                    "If you don't know your skin type, start with a "
                    "simple gentle cleanser, moisturizer and sunscreen."
                )


            # =================================================
            # CONCERNS
            # =================================================

            st.header("🔎 Concern-Based Suggestions")


            if acne:

                st.subheader("🔴 Acne / Pimples")

                st.write("""
                • Gentle cleanser  
                • Non-comedogenic moisturizer  
                • Salicylic acid may help some people  
                • Sunscreen during the day  
                • Avoid squeezing or picking pimples
                """)


            if blackheads:

                st.subheader("⚫ Blackheads")

                st.write("""
                • Gentle cleanser  
                • Salicylic acid may help unclog pores  
                • Non-comedogenic moisturizer  
                • Sunscreen
                """)


            if whiteheads:

                st.subheader("⚪ Whiteheads")

                st.write("""
                • Gentle cleanser  
                • Non-comedogenic products  
                • Salicylic acid may help some people  
                • Moisturizer and sunscreen
                """)


            if pores:

                st.subheader("🕳️ Visible Pores")

                st.write("""
                • Gentle cleanser  
                • Niacinamide may improve the appearance of pores  
                • Lightweight moisturizer  
                • Sunscreen
                """)


            if tan:

                st.subheader("☀️ Tan / Uneven Tone")

                st.write("""
                • Broad-spectrum SPF 30+ sunscreen  
                • Reapply sunscreen when appropriate  
                • Avoid harsh bleaching products  
                • Tinted sunscreen can help protect against visible light
                """)


            if dark_spots:

                st.subheader("🟤 Dark Spots")

                st.write("""
                • Daily sunscreen  
                • Niacinamide may help with uneven pigmentation  
                • Avoid picking acne
                """)


            if dark_circles:

                st.subheader("👁️ Dark Circles")

                st.write("""
                • Gentle skincare around the eye area  
                • Sun protection  
                • Adequate sleep  
                """)


            if excess_oil:

                st.subheader("💧 Excess Oil")

                st.write("""
                • Gentle foaming cleanser  
                • Lightweight moisturizer  
                • Non-comedogenic products  
                • Avoid repeatedly washing your face
                """)


            if dryness:

                st.subheader("🏜️ Dryness")

                st.write("""
                • Gentle hydrating cleanser  
                • Cream-based moisturizer  
                • Avoid harsh scrubs  
                • Sunscreen
                """)


            if redness or irritation:

                st.subheader("🌿 Redness / Irritation")

                st.write("""
                • Gentle fragrance-free cleanser  
                • Simple moisturizer  
                • Avoid harsh scrubs  
                • Avoid introducing many new products at once
                """)

                st.warning(
                    "Persistent or severe redness/irritation should be "
                    "checked by a dermatologist."
                )


            if uneven_texture:

                st.subheader("〰️ Uneven Texture")

                st.write("""
                • Gentle cleanser  
                • Moisturizer  
                • Sunscreen  
                • Avoid aggressive scrubbing
                """)


# =====================================================
# PRODUCT RECOMMENDATIONS
# =====================================================

elif page == "🧴 Product Recommendations":

    st.markdown(
        '<div class="section-title">🧴 Product Guide</div>',
        unsafe_allow_html=True
    )

    product_type = st.selectbox(
        "What product are you looking for?",
        [
            "Face Wash",
            "Serum",
            "Toner",
            "Moisturizer"
        ]
    )

    skin = st.selectbox(
        "Choose your skin type",
        [
            "Oily",
            "Dry",
            "Combination",
            "Normal",
            "Sensitive"
        ]
    )

    if st.button("🔎 Show Suggestions"):

        st.success("Suggestions generated! 🌸")

        if product_type == "Face Wash":

            if skin == "Oily":
                st.write("🧴 Look for: gentle foaming / non-comedogenic cleanser")

            elif skin == "Dry":
                st.write("🧴 Look for: hydrating, fragrance-free cleanser")

            elif skin == "Sensitive":
                st.write("🧴 Look for: gentle fragrance-free cleanser")

            else:
                st.write("🧴 Look for: gentle cleanser suitable for your skin type")


        elif product_type == "Serum":

            if skin == "Oily":
                st.write("✨ Ingredient option: Niacinamide")

            elif skin == "Dry":
                st.write("✨ Ingredient option: Hyaluronic acid")

            elif skin == "Sensitive":
                st.write("✨ Keep it simple: hydrating serum with minimal ingredients")

            else:
                st.write("✨ Ingredient option: simple hydrating serum")


        elif product_type == "Toner":

            st.write("""
            🌸 Choose a gentle, alcohol-free toner.

            Avoid strong toners if your skin is sensitive or irritated.
            """)


        elif product_type == "Moisturizer":

            if skin == "Oily":
                st.write("💧 Lightweight gel/gel-cream, non-comedogenic")

            elif skin == "Dry":
                st.write("💧 Cream-based, fragrance-free moisturizer")

            elif skin == "Sensitive":
                st.write("💧 Fragrance-free moisturizer")

            else:
                st.write("💧 Lightweight moisturizer")


# =====================================================
# SUNSCREEN GUIDE
# =====================================================

elif page == "☀️ Sunscreen Guide":

    st.markdown(
        '<div class="section-title">☀️ Sunscreen Guide</div>',
        unsafe_allow_html=True
    )

    sunscreen_type = st.selectbox(
        "Choose your sunscreen preference",
        [
            "Oily / Acne-Prone",
            "Dry Skin",
            "Sensitive Skin",
            "Tanning / Dark Spots",
            "General Daily Use"
        ]
    )

    if sunscreen_type == "Oily / Acne-Prone":

        st.markdown("""
        ### 💧 Oily / Acne-Prone

        Look for:

        • SPF 30 or higher  
        • Broad-spectrum  
        • Water resistant  
        • Non-comedogenic  
        • Lightweight gel/fluid texture
        """)

    elif sunscreen_type == "Dry Skin":

        st.markdown("""
        ### 🏜️ Dry Skin

        Look for:

        • SPF 30 or higher  
        • Broad-spectrum  
        • Moisturizing cream/lotion texture  
        • Fragrance-free if sensitive
        """)

    elif sunscreen_type == "Sensitive Skin":

        st.markdown("""
        ### 🌿 Sensitive Skin

        Look for:

        • SPF 30 or higher  
        • Broad-spectrum  
        • Fragrance-free  
        • Mineral sunscreen containing zinc oxide and/or titanium dioxide
        """)

    elif sunscreen_type == "Tanning / Dark Spots":

        st.markdown("""
        ### ☀️ Tanning / Dark Spots

        Look for:

        • SPF 30 or higher  
        • Broad-spectrum  
        • Water resistant  
        • Tinted sunscreen containing iron oxide may provide additional
          protection against visible light
        """)

    else:

        st.markdown("""
        ### 🌸 Daily Sunscreen

        Look for:

        • SPF 30+  
        • Broad-spectrum  
        • Water resistant  
        • Comfortable enough to use every day
        """)


# =====================================================
# ROUTINE
# =====================================================

elif page == "🌙 Skincare Routine":

    st.markdown(
        '<div class="section-title">🌙 Your Simple Routine</div>',
        unsafe_allow_html=True
    )

    st.subheader("☀️ Morning")

    st.write("""
    1️⃣ Gentle Face Wash

    2️⃣ Serum (optional)

    3️⃣ Moisturizer

    4️⃣ Broad-spectrum SPF 30+ Sunscreen
    """)

    st.divider()

    st.subheader("🌙 Night")

    st.write("""
    1️⃣ Gentle Face Wash

    2️⃣ Serum / Treatment (if suitable)

    3️⃣ Moisturizer
    """)

    st.info(
        "A simple routine is usually better than using many products at once."
    )


# =====================================================
# SAFETY
# =====================================================

elif page == "⚠️ Safety Information":

    st.markdown(
        '<div class="section-title">⚠️ Safety Information</div>',
        unsafe_allow_html=True
    )

    st.warning("""
    This application is an educational skincare assistant.

    It cannot diagnose skin diseases from a photograph.
    """)

    st.subheader("💊 About Tablets / Medicines")

    st.write("""
    This app does NOT recommend tablets or prescription medicines.

    A face photograph cannot safely determine whether someone needs
    an oral medicine. Medicines for acne and other skin conditions
    should be selected by a qualified healthcare professional.
    """)

    st.subheader("🧴 Patch Testing")

    st.write("""
    When trying a new skincare product, introduce it carefully and
    stop using it if it causes significant irritation.
    """)

    st.subheader("👩‍⚕️ When to See a Dermatologist")

    st.write("""
    Consider professional advice for:

    • Persistent or severe acne
    • Painful or worsening skin problems
    • Persistent redness
    • Severe irritation
    • A changing or unusual skin lesion
    """)

    st.caption(
        "GlowCare AI 🌸 — General skincare information, not medical diagnosis."
    )