import pytest

pytest.main(["-m smoke","--junitxml=HtmlReport/result.xml","--html=HtmlReport/smoke_report.html"])

