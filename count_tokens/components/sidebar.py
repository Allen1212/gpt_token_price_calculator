import streamlit as st


def sidebar():
    with st.sidebar:
        st.markdown("# About")
        st.markdown(
            "🧮**GPT Token Price Calculator** helps you estimate token count and pricing for GPT models based on your uploaded file and/or provided prompt, enabling efficient cost management."
        )
        st.markdown(
            "If you like it, please give [GPT Token Price Calculator](https://github.com/Allen1212/gpt_token_price_calculator.git) a star 🌟."
        )

        st.markdown("💖Thanks💖")

        st.markdown("---")

        st.markdown(
            "## How to use:\n"
            "1. Choose a model 🤖\n"
            "2. Upload a pdf, docx, or txt file📄\n"
            "3. Enter your prompt 🪄\n"
            "4. Calculate the number of tokens and its price 💰\n"
        )

        model = st.selectbox(
            "Which model will you use?",
            (
                "gpt-3.5-turbo",
                "gpt-3.5-turbo-0613",
                "gpt-3.5-turbo-1106",
                "gpt-3.5-turbo-16k",
                "gpt-4-8k",
                "gpt-4-32k",
                "gpt-4-turbo",
                "gpt-4o",
                "gpt-4o-mini",
                "ada",
                "babbage",
                "curie",
                "davinci",
            ),
        )
        st.session_state["MODEL"] = model
