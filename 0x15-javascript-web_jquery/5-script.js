$("DIV#add_item").on('click', function (event) {
	$("UL.my_list").html($("UL.my_list").html() + "<li>Item</li>");
});
