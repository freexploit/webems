$(document).ready(function(evt) {
	$('#absolutify').click(function(evt){
		evt.preventDefault();
		$("#page_to_emulate").removeClass('error');
		$($("#page_to_emulate").find('.help-block')[0]).hide();
		if ($("#url").val() === ""){
			$("#page_to_emulate").addClass('error');
			$($("#page_to_emulate").find('.help-block')[0]).show();
		}
		else{
			var regexes = ['src\=\"\/(?!\/)', 'src\=\"\.\/', 'src\=\'\/(?!\/)', 'src\=\'\.\/', 'href\=\"\/(?!\/)', 'href\=\"\.\/', 'href\=\'\/(?!\/)', 'href\=\'\.\/', 'action\=\"\/(?!\/)', 'action\=\"\.\/',  'action\=\'\/(?!\/)', 'action\=\'\.\/'];
			var replaces = ['src="', 'src="', "src='", "src='", 'href="', 'href="', "href='", "href='", 'action="', 'action="', "action='", "action='"];
			var original = $("#original_html_input").val();
			var url = $("#url").val();
			var base_url = url.substring(0,url.lastIndexOf('/')+1);
			var repl = 'src="';
			var re = new RegExp(regexes[0]);
			for (i in regexes){
				re = new RegExp(regexes[i]);
				repl = replaces[i] + base_url;
				original = original.replace(re, repl);
			}
			$("#modified_html_input").val(original);
			$("#modified_html").fadeIn();
			console.log(original);
		}
	});
	// $(".delete_button").click(function(evt){
	// 	evt.preventDefault();
	// 	var to_delete = $(this).attr('id').split('_')[1];
 //        $.post('/emulations/emulation/' + to_delete + '/delete/', {
 //            data: ""
 //        }, function(data) {
 //            if (data && data.success) {
 //               $('#confirm_delete').modal('toggle');
 //               $('#emulation_deleted').modal('toggle');
 //            }
 //        });
	// });
});