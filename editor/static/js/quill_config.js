// static/js/quill_config.js
var quill = new Quill('#editor', {
    theme: 'snow',
    modules: {
        syntax: true, // Include syntax module
        toolbar: [
            [{ 'header': [1, 2, false] }],
            ['bold', 'italic', 'underline'],
            ['code-block']
        ]
    }
});
