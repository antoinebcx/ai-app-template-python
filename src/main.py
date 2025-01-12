import streamlit as st
import io
from PIL import Image
from ai_services import llm_analysis, audio_transcription, image_to_text

st.set_page_config(page_title='AI app template')


def app():
    """
    Main function that runs the Streamlit app.
    """
    st.markdown(
        "<h2 style='text-align: center;'>AI app template</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align: center;'>This app demonstrates how to use AI services to extract information in a structured way from text, audio, and images.</p>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    text_order_button = False
    audio_order_button = False
    image_order_button = False

    tab1, tab2, tab3 = st.tabs(["Text", "Audio", "Image"])

    with tab1:
        order = st.text_area(
        "Enter a text input",
        "",
        )
        if len(order) > 0:
            text_order_button = st.button("Run text analysis", type="primary")
    
    with tab2:    
        uploaded_audio = st.file_uploader("Upload audio", type=['mp3', 'wav', 'ogg'])
        recorded_audio = st.audio_input("Record", key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
        audio_data = None

        if uploaded_audio is not None:
            st.write("Uploaded audio:")
            st.audio(uploaded_audio, format='audio/wav')
            audio_data = uploaded_audio
            audio_order_button = st.button("Run audio analysis", type="primary")

        elif recorded_audio is not None:
            st.write("Recording:")
            st.audio(recorded_audio, format='audio/wav')
            audio_data = recorded_audio
            audio_order_button = st.button("Run audio analysis", type="primary")

    with tab3:
        uploaded_image = st.file_uploader("Upload an image", type=['png', 'jpg'])
        if uploaded_image:
            image_bytes = uploaded_image.getvalue()
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image)
            image_order_button = st.button("Run image analysis", type="primary")        
    
    st.markdown("<br>", unsafe_allow_html=True)

    if text_order_button or audio_order_button or image_order_button:
        if audio_order_button:
            with st.spinner(f"Transcribing audio... \n\n"):
                transcript = audio_transcription(audio_data)
                if transcript:
                    st.markdown(f"<h4 style='text-align: center;'>Transcript</h4>", unsafe_allow_html=True)
                    st.markdown(transcript)
                    st.markdown("<br>", unsafe_allow_html=True)
                    order = transcript

        if image_order_button:
            with st.spinner(f"Extracting text from image... \n\n"):
                extraction = image_to_text(uploaded_image)
                if extraction:
                    st.markdown(f"<h4 style='text-align: center;'>Extracted text from image</h4>", unsafe_allow_html=True)
                    st.markdown(extraction)
                    st.markdown("<br>", unsafe_allow_html=True)
                    order = extraction

        try:
            with st.spinner(f"Analyzing the input... \n\n"):
                analysis_result = llm_analysis(order)
                
                st.markdown(f"<h4 style='text-align: center;'>Analysis</h4>", unsafe_allow_html=True)
                st.write(st.write(analysis_result.model_dump()))

        except Exception as e:
            st.write(
                "Error during the process. Please reload below and try again."
            )
            st.write(
                {e}
            )
            if st.button("Reload"):
                st.experimental_rerun()
            st.stop()


hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)


if __name__ == "__main__":
    app()
