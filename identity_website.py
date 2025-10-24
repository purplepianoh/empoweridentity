import streamlit as st
import random

st.markdown("""
<style>
/* Main app and body background */
.stApp {
    background-color: #FFEBEB !important;
}

/* Main text (headings, paragraphs, labels) */
body, h1, h2, h3, h4, h5, h6, .stMarkdown, .stTextInput > label, .stMultiselect > label, .stCheckbox > label {
    color: #C71585 !important; /* Medium violet red for text */
    font-family: 'Arial', sans-serif; /* Clean font for readability */
}

/* Center title */
div.st-key-app_title div.stHeading {
    text-align: center;
}

/* Input fields and selectboxes text */
.stTextInput input, .stMultiselect div[role='combobox'] {
    color: #C71585 !important; /* Pink text in inputs */
    background-color: #FFF !important; /* White background for inputs for contrast */
}

/* Styling the dropdown list when it's open */
ul[data-testid="stSelectboxVirtualDropdown"] {
    background-color: white !important;
    border: 1px solid #ccc !important;
}

/* Affirmation output (success message) */
.stAlert {
    background-color: #FFF0F5 !important; /* Light pink for success box */
    color: #C71585 !important; /* Darker pink text */
    border: 1px solid #FF69B4 !important; /* Hot pink border */
}

/* Button styling */
.stButton > button {
    background-color: #FF69B4 !important; /* Hot pink button */
    color: #FFF !important; /* White text on button */
    border: 1px solid #C71585 !important;
}

/* Hover effect for buttons */
.stButton > button:hover {
    background-color: #E75480 !important; /* Darker pink on hover */
    color: #FFF !important;
}

/* Balloons for fun (optional tweak to make them pinker) */
.stBalloons {
    filter: hue-rotate(330deg); /* Shift balloons toward pink hue */
}
</style>
""", unsafe_allow_html=True)

# Expanded lists for more variety and flexibility
roles = [
    "student", "artist", "leader", "explorer", "teacher", "entrepreneur", 
    "athlete", "writer", "musician", "scientist", "caregiver", "innovator", "volunteer", 
    "dreamer", "builder", "healer", "adventurer", "mentor", "friend"
]
strengths = [
    "resilient", "creative", "empowered", "unique", "brave", "compassionate", "intelligent", 
    "adaptable", "passionate", "determined", "optimistic", "resourceful", "kind", "bold", 
    "patient", "visionary", "loyal", "energetic", "wise", "humorous"
]
challenges = [
    "doubt", "fear", "setbacks", "uncertainty", "loneliness", "stress", "failure", 
    "change", "pressure", "loss", "anxiety", "rejection", "overwhelm", "confusion", 
    "frustration", "isolation", "distrust", "insecurity", "exhaustion", "dilemmas"
]
actions = [
    "embrace your journey", "inspire those around you", "conquer any obstacle", 
    "trust your intuition", "build meaningful connections", "celebrate your wins", 
    "learn from every experience", "stay true to yourself", "push beyond limits", 
    "find joy in the process", "lead with heart", "adapt and thrive", 
    "create your own path", "support others along the way", "reflect and grow", 
    "face fears head-on", "cultivate inner peace", "innovate solutions", 
    "honor your values", "persist with grace"
]
emojis = ["💪", "🌈", "🔥", "🌟", "🚀", "❤️", "🦋", "🌻", "🏆", "🧠", "✨", "⚡", "🌊", "🗝️"]
motivational_quotes = [
    "“Your unique identity is your greatest strength—embrace it fully.”",
    "“Every facet of who you are fuels your journey to greatness.”",
    "“Be unapologetically you; your authenticity lights the way.”",
    "“Your identity is a mosaic—each piece makes you extraordinary.”",
    "“Embrace all that you are; your story inspires others.”",
    "“Your strengths define your path; let them guide you forward.”",
    "“Who you are today is the foundation for who you’ll become.”",
    "“Your identity is your power—wield it with courage.”",
    "“Every challenge you face shapes the masterpiece of you.”",
    "“Celebrate your unique self; you are enough.”",
    "“Believe you can and you're halfway there.” — Theodore Roosevelt",
    "“The only person you are destined to become is the person you decide to be.” — Ralph Waldo Emerson",
    "“The question isn't who is going to let me; it's who is going to stop me.” — Ayn Rand",
    "“Winning is not a sometime thing; it's an all the time thing.” — Vince Lombardi",
    "“Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.” — Christian D. Larson",
    "“You miss 100% of the shots you don't take.” — Wayne Gretzky",
    "“I alone cannot change the world, but I can cast a stone across the water to create many ripples.” — Mother Teresa",
    "“You become what you believe.” — Oprah Winfrey",
    "“The most difficult thing is the decision to act, the rest is merely tenacity.” — Amelia Earhart",
    "“How wonderful it is that nobody need wait a single moment before starting to improve the world.” — Anne Frank",
    "“The unexamined life is not worth living.” — Socrates",
    "“Everything you've ever wanted is on the other side of fear.” — George Addair",
    "“Dream big and dare to fail.” — Norman Vaughan",
    "“It does not matter how slowly you go as long as you do not stop.” — Confucius",
    "“Hardships often prepare ordinary people for an extraordinary destiny.” — C.S. Lewis",
    "“Too many of us are not living our dreams because we are living our fears.” — Les Brown",
    "“I have learned over the years that when one's mind is made up, this diminishes fear.” — Rosa Parks",
    "“If you're offered a seat on a rocket ship, don't ask what seat! Just get on.” — Sheryl Sandberg",
    "“I attribute my success to this: I never gave or took any excuse.” — Florence Nightingale",
    "“Dreaming, after all, is a form of planning.” — Gloria Steinem",
    "“Whatever the mind of man can conceive and believe, it can achieve.” — Napoleon Hill",
    "“Twenty years from now, you will be more disappointed by the things you didn't do than by the ones you did. So, throw off the bowlines, sail away from safe harbor, catch the trade winds in your sails. Explore. Dream. Discover.” — Mark Twain"
]

# Affirmation templates for variety
affirmation_templates = [
    "{name}, your {strengths_str} spirit as a {roles_str} empowers you to conquer {challenges_str} as you {action}! {emoji}",
    "As a {roles_str}, {name}, your {strengths_str} nature shines, helping you overcome {challenges_str} to {action}. {emoji}",
    "To {name}, the {roles_str}: Your {strengths_str} essence drives you to rise above {challenges_str} as you {action}. {emoji}",
    "{name}, with your {strengths_str} character as a {roles_str}, you transform {challenges_str} as you {action}. {emoji}",
    "Embrace your {strengths_str} identity, {name}! As a {roles_str}, you navigate {challenges_str} to {action}. {emoji}",
    "{name}, your journey as a {roles_str} is fueled by your {strengths_str} heart, allowing you to surpass {challenges_str} as you {action}! {emoji}",
    "Being {strengths_str} as a {roles_str}, {name}, you face {challenges_str} head-on, thriving to {action}. {emoji}",
    "Shine bright, {name}! Your {strengths_str} soul as a {roles_str} lifts you above {challenges_str} as you {action}. {emoji}",
    "{name}, the {roles_str}, channels a {strengths_str} mindset to overcome {challenges_str}, succeeding as you {action}! {emoji}",
    "With your {strengths_str} core, {name}, you soar as a {roles_str}, conquering {challenges_str} to {action}. {emoji}"
]
with st.container(key="app_title"):
    st.title("🌟 Empower Your Identity 🌟")

st.markdown("""
Welcome! Discover your identity by selecting multiple roles, strengths, and challenges. 
We'll generate a personalized affirmation, just for you!
""")

# Inputs with multiselect for flexibility
name = st.text_input("Your name (optional):", placeholder="Enter your name or leave blank")

selected_roles = st.multiselect(
    "Select parts of your identity roles (click multiple):",
    options=roles,
    placeholder="Choose role(s)"
)

selected_strengths = st.multiselect(
    "Select your key strengths (click multiple):",
    options=strengths,
    placeholder="Choose strength(s)"
)

# Allow predefined challenges or custom input
use_custom_challenge = st.checkbox("Add a custom challenge instead of selecting?", value=False)
if use_custom_challenge:
    custom_challenge = st.text_input("Your custom challenge:", placeholder="Describe your challenge")
    selected_challenges = [custom_challenge] if custom_challenge else []
else:
    selected_challenges = st.multiselect(
        "Select challenges you're facing (click multiple):",
        options=challenges,
        placeholder="Choose challenge(s)"
    )

# Button to generate
if st.button("Generate Affirmation"):
    if not selected_roles or not selected_strengths or not selected_challenges:
        st.warning("Please select at least one role, strength, and challenge!")
    else:
        # Format selections with commas and "and" for natural grammar
        def format_list(items, fallback):
            if not items:
                return fallback
            # If 4 or more items, randomly select up to 3
            if len(items) >= 4:
                items = random.sample(items, min(3, len(items)))
            if len(items) == 1:
                return items[0]
            if len(items) == 2:
                return f"{items[0]} and {items[1]}"
            return f"{', '.join(items[:-1])}, and {items[-1]}"

        roles_str = format_list(selected_roles, "individual")
        strengths_str = format_list(selected_strengths, "spirit")
        challenges_str = format_list(selected_challenges, "hurdles")
        
        # Random selections for variety
        action = random.choice(actions)
        emoji = random.choice(emojis)
        template = random.choice(affirmation_templates)
        quote = random.choice(motivational_quotes)
        
        # Generate affirmation
        name_str = name if name else "you"
        affirmation = template.format(
            name=name_str,
            roles_str=roles_str,
            strengths_str=strengths_str,
            challenges_str=challenges_str,
            action=action,
            emoji=emoji
        )
        full_output = f"{affirmation}\n\n*{quote}*"

        st.success(full_output)
        st.balloons()  # Fun visual feedback