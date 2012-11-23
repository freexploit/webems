$(document).ready(function(evt) {
	$("#modified_html_input").keyup(function(){
		$("#save").button('reset');
	});
	$("#url").keyup(function(){
		$("#save").button('reset');
	});
	$("#name").keyup(function(){
		$("#save").button('reset');
	});
	$("#original_html_input").keyup(function(){
		$("#save").button('reset');
	});
	$('.edit_disabled').click(function(evt){
		evt.preventDefault();
		$(this).hide();
		$(this).parent().next().removeAttr('disabled');
	});
	$("#save").click(function(evt){
		evt.preventDefault();
		//clear any validation errors
		$("#page_to_emulate").removeClass('error');
		$($("#page_to_emulate").find('.help-block')[0]).hide();
		$("#name_group").removeClass('error');
		$($("#name_group").find('.help-block')[0]).hide();
		$("#modified_html_group").removeClass('error');
		$($("#modified_html_group").find('.help-block')[0]).hide();
		//make sure inputs are present
		var go = true;
		if ($("#url").val() === ""){
			$.scrollTo("#url", { offset: {top:-80, left:0} });
			$("#page_to_emulate").addClass('error');
			$($("#page_to_emulate").find('.help-block')[0]).show();
			go = false;
		}
		if ($("#name").val() === ""){
			$("#name_group").addClass('error');
			$($("#name_group").find('.help-block')[0]).show();
			go = false;
		}
		if ($("#modified_html_input").val() === ""){
			$("#modified_html_group").addClass('error');
			$($("#modified_html_group").find('.help-block')[0]).show();
			go = false;
		}
		if (go){
			$(this).button('loading');
			var data = {};
			var id = parseInt($("form").attr("id"));
			data["id"] = id;
			data["url"] = $("#url").val();
            data["name"] = $("#name").val();
            data["html"] = $("#modified_html_input").val();
            data["original_html"] = $("#original_html_input").val();
            data = $.toJSON(data);
	        $.post('/emulations/emulation/' + id + '/modify/', {
	            data : data
	        }, function(data) {
	            if (data && data.success) {
	               $("#save").button('complete');
	               $('#create_success').modal('toggle');
	               $('#delete_emulation').attr('href', '/emulations/emulation/' + data.id + '/delete/');
	               $('#edit_emulation').attr('href', '/emulations/emulation/' + data.id + '/edit/');
	               $('#view_emulation').attr('href', '/emulations/emulation/' + data.id + '/view/');
	            }
	        });
		}
	});
});