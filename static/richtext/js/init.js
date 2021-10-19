'use strict';

{
    // Editor id
    let editor_id = 'td92-rich-text-id'

    // Plugins
    let plugins = 'autoresize nonbreaking searchreplace fullpage ' +
        'lists advlist checklist table directionality hr codesample image link autolink preview fullscreen'

    // Toobar
    let toolbar = 'undo redo ' +
        'formatselect fontselect fontsizeselect bold italic ' +
        'alignleft aligncenter alignright alignjustify ' +
        'indent outdent ' +
        'numlist bullist checklist ' +
        'forecolor backcolor ' +
        'table ' +
        'ltr rtl ' +
        'image ' +
        'link unlink ' +
        'removeformat hr ' +
        'blockquote ' +
        'codesample ' +
        'preview fullscreen '

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
        }
    );
    editor.on('init', function (e) {
        editor.container.classList.add('td92-rich-text-class');
    })
    editor.render();
}
