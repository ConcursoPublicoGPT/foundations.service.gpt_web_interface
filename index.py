from src.configs.page_config import PageConfig
from src.widgets.header_widget import HeaderWidget
from src.widgets.topic_selector_widget import TopicSelectorWidget
from src.widgets.chat_widget import ChatWidget

PageConfig.set()
HeaderWidget.display()
selected_topic = TopicSelectorWidget.display()
ChatWidget.display(selected_topic)
