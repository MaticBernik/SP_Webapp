function popitup(url,name="name") {
	newwindow=window.open(url,name,'height=200,width=150');
	if (window.focus) {newwindow.focus()}
	return false;
}

