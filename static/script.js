$(document).ready(function() {
    $('#uploadForm').on('submit', function(e) {
        e.preventDefault();
        
        var fileInput = $('#file')[0];
        var file = fileInput.files[0];
        if (file.type !== 'application/vnd.ms-excel' && file.type !== 'text/csv') {
            $('#message').text('Uploaded file is not supported. Please upload a .csv file.');
            return;
        }

        $('#message').text('Please Wait! File is converting...');
        $('#convertButton button').hide();
        $('#delimiterField').hide();
        $('#fileField').hide();
        $('#spinner').show(); 

        var formData = new FormData(this);

        $.ajax({
            url: '/convert',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                $('#message').text('File conversion complete.');
                $('#downloadLink').html('<a href="' + response.download_url + '" class="bg-green-500 text-white p-2 rounded-md">Download Converted File</a>');
                $('#tryAgainButton').show();
            },
            error: function() {
                $('#message').text('An error occurred during file conversion.');
                $('#tryAgainButton').show();
            },
            complete: function() {
                $('#spinner').hide();
            }
        });
    });
});

function resetForm() {
    $('#message').text('');
    $('#downloadLink').html('');
    $('#tryAgainButton').hide();
    $('#uploadForm')[0].reset();
    $('#convertButton button').show();
    $('#delimiterField').show();
    $('#fileField').show();
}
