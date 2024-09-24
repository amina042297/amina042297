import streamlit as st
from functions import extract_text_from_ppt, extract_text_from_pdf, merge_pdfs, check_statements, load_model, get_pdf_image, combine_model_results

# Title and main header
st.markdown("<h1 style='text-align: center; color: #FF6347;'>Statement Correctness Checker</h1>", unsafe_allow_html=True)

# File uploader section
st.markdown("<h3 style='color: #4682B4;'>Upload Your Files</h3>", unsafe_allow_html=True)
uploaded_files = st.file_uploader("Upload PPT or PDF files", type=["pptx", "pdf"], accept_multiple_files=True)

if uploaded_files:
    pdf_files = [file for file in uploaded_files if file.name.endswith(".pdf")]
    merged_pdf = merge_pdfs(pdf_files) if pdf_files else None

    slides = []
    for file in uploaded_files:
        if file.name.endswith(".pptx"):
            slides.extend(extract_text_from_ppt(file))
        elif file.name.endswith(".pdf"):
            slides.extend(extract_text_from_pdf(file))
    
    st.markdown("<h3 style='color: #32CD32;'>Files Uploaded Successfully!</h3>", unsafe_allow_html=True)

    # Statement input and settings section
    st.markdown("<h3 style='color: #4682B4;'>Check Statements</h3>", unsafe_allow_html=True)
    statement_input = st.text_area("Enter statements to check (separate each statement with a new line):")
    threshold_range = st.slider('Set Ambiguity Thresholds', 0.0, 1.0, (0.40, 0.60), key='thresholds')
    use_gpt = st.checkbox('Use GPT for ambiguous cases', value=True)

    if st.button('Check Statements'):
        statements = statement_input.strip().split("\n")
        model = load_model()
        results = combine_model_results(slides, statements, model, use_gpt, threshold_range[0], threshold_range[1])
        
        st.markdown("<h3 style='color: #4682B4;'>Results</h3>", unsafe_allow_html=True)
        for statement, result in results.items():
            color = "green" if result["result"] == "True" else "red"
            gpt_info = f", GPT: {result.get('gpt_result', 'N/A')}" if use_gpt and threshold_range[0] <= result['similarity'] <= threshold_range[1] else ""
            st.markdown(f"<span style='color:{color}'>{statement}</span>: {result['result']} (Similarity: {result['similarity']:.2f}{gpt_info}, Slide: {result['slide_number']})", unsafe_allow_html=True)
            if result['slide_number']:
                img = get_pdf_image(merged_pdf, result['slide_number'])
                if img:
                    st.image(img)

    if merged_pdf:
        st.markdown("<h3 style='color: #4682B4;'>Download Merged PDF</h3>", unsafe_allow_html=True)
        st.download_button(label="Download Merged PDF", data=merged_pdf, file_name="merged.pdf")

        


# footer
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f0f0f0;
        color: black;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        <p>Developed by <a href="mailto:amina22@bu.edu">Amina Bauyrzhan</a></p>
    </div>
    """, unsafe_allow_html=True)
