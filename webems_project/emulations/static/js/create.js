String.prototype.splice = function( idx, rem, s ) {
	return (this.slice(0,idx) + s + this.slice(idx + Math.abs(rem)));
};

$(document).ready(function(evt) {
	$('#absolutify').click(function(evt){
		evt.preventDefault();
		$("#page_to_emulate").removeClass('error');
		$($("#page_to_emulate").find('.help-block')[0]).hide();
		if ($("#url").val() === ""){
			$.scrollTo("#url", { offset: {top:-80, left:0} });
			$("#page_to_emulate").addClass('error');
			$($("#page_to_emulate").find('.help-block')[0]).show();
			$("#page_to_emulate").focus();
		}
		else{
			// var regexes = ['src\=\"\/(?!\/)', 'src\=\"\.\/', 'src\=\'\/(?!\/)', 'src\=\'\.\/', 'href\=\"\/(?!\/)', 'href\=\"\.\/', 'href\=\'\/(?!\/)', 'href\=\'\.\/', 'action\=\"\/(?!\/)', 'action\=\"\.\/',  'action\=\'\/(?!\/)', 'action\=\'\.\/'];
			// var replaces = ['src="', 'src="', "src='", "src='", 'href="', 'href="', "href='", "href='", 'action="', 'action="', "action='", "action='"];
			var original = $("#original_html_input").val();
			var url = $("#url").val();
			var base_url = url.substring(0,url.lastIndexOf('/')+1);
			//add a base tag using custom string splice function to insert it after the head element
			original = original.splice((original.indexOf('>', original.indexOf("<head"))+1), 0, '<base href="' + base_url + '"/>');
			// var repl = 'src="';
			// var re = new RegExp(regexes[0]);
			// for (i in regexes){
			// 	re = new RegExp(regexes[i]);
			// 	repl = replaces[i] + base_url;
			// 	original = original.replace(re, repl);
			// }
			$("#modified_html_input").val(original);
			$("#modified_html").fadeIn();
		}
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
			var info = {};
			info["url"] = $("#url").val();
			info["name"] = $("#name").val();
			info["html"] = $("#modified_html_input").val();
			info["original_html"] = $("#original_html_input").val();
			var data = $.toJSON(info);
			$.ajax({
				type: "POST",
				url : '/emulations/emulation/save/', 
				data : data,
				success: function(data) {
					if (data && data.success) {
						$('#create_success').modal('toggle');
						$('#delete_emulation').attr('href', '/emulations/emulation/' + data.id + '/delete/');
						$('#edit_emulation').attr('href', '/emulations/emulation/' + data.id + '/edit/');
						$('#view_emulation').attr('href', '/emulations/emulation/' + data.id + '/view/');
						$('#new_emulation_id').text(data.id);
						$('#new_emulation_name').text(info['name']);
						$('#new_emulation_url').text(info['url']);
						var url = location.protocol + "//" + location.host + "/emulations/emulation/"+ data.id + "/view/";
						$("#new_emulation_link").text(url);
					}
					else{
						$('.alert').show();
					}
				},
				error: function(){
					$('.alert').show();
				},
			});
		}
	});
	$("#delete_emulation").click(function(evt){
		evt.preventDefault();
		var em_id = $("#new_emulation_id").text();
        $.post('/emulations/emulation/' + em_id + '/delete/', {
            data: ""
        }, function(data) {
            if (data && data.success) {
               $('#create_success').modal('toggle');
               $('#emulation_deleted').modal('toggle');
            }
        });
	});
	$("#confirm_deleted").click(function(evt){
		evt.preventDefault();
		window.location.reload();
	});
});