<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head profile="http://selenium-ide.openqa.org/profiles/test-case">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="selenium.base" href="http://localhost:8000/library/" />
<title>utsrelease</title>
</head>
<body>
<table cellpadding="1" cellspacing="1" border="1">
<thead>
<tr><td rowspan="1" colspan="3">utsrelease</td></tr>
</thead><tbody>
<tr>
	<td>open</td>
	<td>/library/</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>id=id_username</td>
	<td>genovefa</td>
</tr>
<tr>
	<td>type</td>
	<td>id=id_password</td>
	<td>geslo123</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>id=loginButton</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>id=booksButton</td>
	<td></td>
</tr>
<tr>
	<td>click</td>
	<td>id=newBookButton</td>
	<td></td>
</tr>
<tr>
	<td>waitForPopUp</td>
	<td>name</td>
	<td>30000</td>
</tr>
<tr>
	<td>selectWindow</td>
	<td>name=name</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>id=id_title</td>
	<td>TestnaKnjiga</td>
</tr>
<tr>
	<td>select</td>
	<td>id=id_author</td>
	<td>label=Eoin Colfer</td>
</tr>
<tr>
	<td>type</td>
	<td>id=id_genre</td>
	<td>drama</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>id=newBookButton</td>
	<td></td>
</tr>
<tr>
	<td>close</td>
	<td></td>
	<td></td>
</tr>
<tr>
	<td>selectWindow</td>
	<td>null</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>id=leasesButton</td>
	<td></td>
</tr>
<tr>
	<td>click</td>
	<td>id=newLeaseButton</td>
	<td></td>
</tr>
<tr>
	<td>waitForPopUp</td>
	<td>name</td>
	<td>30000</td>
</tr>
<tr>
	<td>selectWindow</td>
	<td>name=name</td>
	<td></td>
</tr>
<tr>
	<td>select</td>
	<td>id=id_user</td>
	<td>label=mbresk</td>
</tr>
<tr>
	<td>select</td>
	<td>id=id_book</td>
	<td>label=Eoin Colfer: TestnaKnjiga</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>id=newLeaseButton</td>
	<td></td>
</tr>
<tr>
	<td>close</td>
	<td></td>
	<td></td>
</tr>
<tr>
	<td>selectWindow</td>
	<td>null</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>id=leasesButton</td>
	<td></td>
</tr>
<tr>
	<td>assertElementPresent</td>
	<td>//div[@id='content']/table/tbody/tr[6]/td[3]</td>
	<td>15 Eoin Colfer: TestnaKnjiga</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>name=deleteTestnaKnjiga</td>
	<td></td>
</tr>
<tr>
	<td>assertElementNotPresent</td>
	<td>//div[@id='content']/table/tbody/tr[6]/td[3]</td>
	<td>15 Eoin Colfer: TestnaKnjiga</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>id=booksButton</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>name=deleteTestnaKnjiga</td>
	<td></td>
</tr>
<tr>
	<td>assertElementNotPresent</td>
	<td>//div[@id='content']/table/tbody/tr[8]/td[2]</td>
	<td>TestnaKnjiga</td>
</tr>

</tbody></table>
</body>
</html>
