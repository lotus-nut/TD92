'use strict';

{
    // Editor id
    let editor_id = 'td92-rich-text-id'

    // Plugins
    let plugins = 'autoresize nonbreaking searchreplace fullpage ' +
        'lists advlist checklist table directionality hr codesample image link autolink preview fullscreen code'

    // Toobar
    let toolbar = 'undo redo ' +
        'styleselect fontselect fontsizeselect bold italic ' +
        'alignleft aligncenter alignright alignjustify ' +
        'indent outdent ' +
        'numlist bullist checklist ' +
        'forecolor backcolor ' +
        'table ' +
        'ltr rtl ' +
        'image ' +
        'link unlink ' +
        'removeformat hr ' +
        'superscript subscript ' +
        'blockquote ' +
        'codesample ' +
        'preview fullscreen code'

    // let mobileToolbar = toolbar;

    // Create and init editor
    let editor = tinymce.createEditor(editor_id,
        {
            menubar: false,
            plugins: plugins,
            toolbar: toolbar,

            mobile: {
                toolbar: toolbar,

            },

            // nonbreaking
            nonbreaking_force_tab: true,
            // link
            link_title: false,
            default_link_target: '_blank',
            link_assume_external_targets: 'http',
            // image
            image_advtab: true,
            images_upload_url: '/note/upload_file',
            images_upload_credentials: true,
            automatic_uploads: true,
            image_description: false,
            images_reuse_filename: true,
            image_caption: false,
            image_title: false,
            // fullpage
            fullpage_default_font_size: '12pt',
            fullpage_default_font_family: "'Times New Roman', Georgia;",
            //
            placeholder: "...",
            contextmenu: false,
            toolbar_sticky: true,
            statusbar: false,
            language: 'zh_CN',
            icons: 'custom',
            skin_url: '/static/tinymce-skins/ui_5.1.0',

            style_formats: [
                {
                    title: 'Headers', items: [
                        {title: 'Heading 1', block: 'h1'},
                        {title: 'Heading 2', block: 'h2'},
                        {title: 'Heading 3', block: 'h3'},
                        {title: 'Heading 4', block: 'h4'},
                        {title: 'Heading 5', block: 'h5'},
                        {title: 'Heading 6', block: 'h6'}
                    ]
                },
                {
                    title: 'Inline', items: [
                        {title: 'Underline', format: 'underline'},
                        {title: 'Strikethrough', format: 'strikethrough'},
                        {title: 'Bold', format: 'bold'},
                        {title: 'Italic', format: 'italic'},
                        {title: 'Address', format: 'address'},
                        {title: 'Code', format: 'code'},
                    ],
                },
                {
                    title: 'Blocks', items: [
                        {title: 'Paragraph', block: 'p'},
                        {title: 'Blockquote', block: 'blockquote'},
                        {title: 'Preformatted', block: 'pre'}
                    ],
                },
            ],

        }
    );
    editor.on('init', function (e) {
        editor.container.classList.add('td92-rich-text-class');
    })
    editor.render();
}
