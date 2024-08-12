chrome.runtime.onInstalled.addListener(() => {
    console.log("Extension installed, creating context menu...");
    chrome.contextMenus.create({
        id: "analyzeSentiment",
        title: "Analyze Sentiment on Twitter",
        contexts: ["selection"]
    });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
    console.log("Context menu clicked", info, tab);
    if (info.menuItemId === "analyzeSentiment") {
        const selectedText = info.selectionText;
        chrome.tabs.create({
            url: `http://127.0.0.1:5000/sentiment?topic=${encodeURIComponent(selectedText)}`
        });
    }
});
