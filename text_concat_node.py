class TextConcatenate:
    """
    A ComfyUI node for concatenating multiple text strings with an optional separator.
    Supports up to 10 optional text inputs.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "text_1": ("STRING", {"default": "", "multiline": True}),
                "text_2": ("STRING", {"default": "", "multiline": True}),
                "text_3": ("STRING", {"default": "", "multiline": True}),
                "text_4": ("STRING", {"default": "", "multiline": True}),
                "text_5": ("STRING", {"default": "", "multiline": True}),
                "text_6": ("STRING", {"default": "", "multiline": True}),
                "text_7": ("STRING", {"default": "", "multiline": True}),
                "text_8": ("STRING", {"default": "", "multiline": True}),
                "text_9": ("STRING", {"default": "", "multiline": True}),
                "text_10": ("STRING", {"default": "", "multiline": True}),
                "separator": ("STRING", {"default": "", "multiline": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("concatenated_text",)
    FUNCTION = "concatenate"
    CATEGORY = "text"

    def concatenate(
        self,
        text_1="",
        text_2="",
        text_3="",
        text_4="",
        text_5="",
        text_6="",
        text_7="",
        text_8="",
        text_9="",
        text_10="",
        separator=""
    ):
        # Collect all non-empty text inputs
        texts = [
            text_1, text_2, text_3, text_4, text_5,
            text_6, text_7, text_8, text_9, text_10
        ]
        
        # Filter out empty strings
        non_empty_texts = [t for t in texts if t and t.strip()]
        
        # Join with separator
        result = separator.join(non_empty_texts)
        
        return (result,)


# Node class mappings for ComfyUI
NODE_CLASS_MAPPINGS = {
    "TextConcatenate": TextConcatenate
}

# Display name mappings for ComfyUI
NODE_DISPLAY_NAME_MAPPINGS = {
    "TextConcatenate": "Text Concatenate D"
}

