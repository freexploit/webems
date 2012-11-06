$(document).ready(function(evt) {
	$('.delete').click(function(evt){
		evt.preventDefault();
		var em_id = $(this).closest('tr').attr('id');
		var em_url = $($(this).closest('tr').find('.emulation_url')[0]).text();
		$("#emulation_id").text(em_id);
		$("#emulation_url").text(em_url);
		$(".delete_button").attr('id', "rm_" + em_id);
		$('#confirm_delete').modal('toggle');
	});
	$(".delete_button").click(function(evt){
		evt.preventDefault();
		var to_delete = $(this).attr('id').split('_')[1];
        $.post('/emulations/emulation/' + to_delete + '/delete/', {
            data: ""
        }, function(data) {
            if (data && data.success) {
               $('#confirm_delete').modal('toggle');
               $('#emulation_deleted').modal('toggle');
            }
        });
	});
	$("#confirm_deleted").click(function(evt){
		evt.preventDefault();
		window.location.reload();
	});
	$('.myemulations').click(function(evt){
		evt.preventDefault();
		var em_id = $(this).closest('tr').attr('id');
        $.post('/emulations/emulation/' + em_id + '/myemulations/', {
            data: ""
        }, function(data) {
            if (data && data.success) {
               console.log('success');
            }
        });
	});
});