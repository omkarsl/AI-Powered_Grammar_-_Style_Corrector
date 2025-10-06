import streamlit as st
import language_tool_python
import difflib
import re

tool = language_tool_python.LanguageTool('en-US')

def collapse_repeated_words(text):
    return re.sub(r'\b(\w+)(\s+\1\b)+', r'\1', text, flags=re.IGNORECASE)

def replace_weak_phrases(text):
    replacements = {
        "in order to": "to",
        "due to the fact that": "because",
        "as a matter of fact": "in fact",
        "a lot of": "many",
        "at the end of the day": "in the end",
        "very good": "excellent",
        "very bad": "terrible",
        "basically": "",
        "actually": ""
    }
    for k, v in replacements.items():
        pattern = r'\b' + re.escape(k) + r'\b'
        text = re.sub(pattern, v, text, flags=re.IGNORECASE)
    return text

def style_improve(text):
    before = text
    text = collapse_repeated_words(text)
    text = replace_weak_phrases(text)
    changes = []
    if text != before:
        changes.append("Applied simple style replacements.")
    return text, changes

def grammar_check(text):
    matches = tool.check(text)
    corrected = language_tool_python.utils.correct(text, matches)
    explanations = []
    for m in matches:
        explanations.append({
            "message": m.message,
            "replacements": m.replacements,
            "context": text[max(0, m.offset-30): m.offset + (m.errorLength or 0) + 30]
        })
    return corrected, explanations

def make_diff_html(a, b):
    differ = difflib.HtmlDiff(tabsize=4, wrapcolumn=80)
    a_lines = a.splitlines()
    b_lines = b.splitlines()
    html = differ.make_table(a_lines, b_lines, fromdesc='Original', todesc='Corrected', context=True, numlines=1)
    html = f"<div style='font-family: Arial, sans-serif; font-size: 14px;'>{html}</div>"
    return html

st.set_page_config(page_title="AI Grammar & Style Corrector", layout="wide")
st.title("📝 AI Grammar & Style Corrector — Simple Version")
st.write("Paste text below and click **Correct**. This uses LanguageTool + simple style rules.")

text = st.text_area("Enter text here", height=220)

col1, col2 = st.columns([1,1])
with col1:
    st.subheader("Options")
    auto_apply_style = st.checkbox("Apply simple style improvements", value=True)
    show_explanations = st.checkbox("Show grammar explanations", value=True)
    show_diff = st.checkbox("Show inline diff", value=True)

if st.button("Correct"):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        corrected_grammar, explanations = grammar_check(text)
        final_text = corrected_grammar
        style_changes = []
        if auto_apply_style:
            final_text, style_changes = style_improve(final_text)

        st.subheader("Result")
        left, right = st.columns(2)
        with left:
            st.markdown("**Original**")
            st.write(text)
        with right:
            st.markdown("**Corrected**")
            st.write(final_text)

        if show_explanations:
            st.subheader("Grammar Explanations")
            if explanations:
                for i, ex in enumerate(explanations[:30], 1):
                    st.write(f"**{i}.** {ex['message']} — suggestions: {ex['replacements']}  \n_Context:_ ...{ex['context']}...")
            else:
                st.write("No grammar issues found by LanguageTool.")

        if show_diff:
            st.subheader("Visual Diff")
            diff_html = make_diff_html(text, final_text)
            st.components.v1.html(diff_html, height=300, scrolling=True)

        st.download_button("Download corrected text", final_text, file_name="corrected.txt")
