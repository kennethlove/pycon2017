var $description = $('#id_description');
$('#wysiwyg').trumbowyg()
    .on('tbwinit', function() { $description.hide(); })
    .on('tbwchange', function(e) { $description.val(e.target.innerHTML); });
