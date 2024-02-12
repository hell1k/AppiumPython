import uiautomator2 as u


def test_example():
    d = u.connect("emulator-5554")
    # d = u.connect("49e9905f")
    d(resourceId="com.yapmap.yapmap:id/sign_in_button").click()
    d.xpath('//*[@resource-id="com.yapmap.yapmap:id/email_edit_text_layout"]/android.widget.FrameLayout[1]').set_text("qwe")

