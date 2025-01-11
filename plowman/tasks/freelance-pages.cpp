#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <map>

class ArticleManager {
private:
    std::string articleText;
    std::vector<std::string> pages;
    std::vector<std::string> pageLines;
    std::vector<std::string> words;
    std::map<std::string, int> options;
    int paidPages;

    // Helper function to split a string into words
    std::vector<std::string> splitWords(const std::string &text) {
        std::istringstream stream(text);
        std::vector<std::string> result;
        std::string word;
        while (stream >> word) {
            result.push_back(word);
        }
        return result;
    }

public:
    ArticleManager(const std::string &articleText,
        const std::map<std::string, int>& options = std::map<std::string, int>()) 
        : articleText(articleText), options(options), paidPages(0) {}

    void splitIntoPages() {
        // Split article text into words
        words = splitWords(articleText);

        std::cout << "Total words: " << words.size() << std::endl;

        // Create lines from words
        std::vector<std::string> lines;
        for (size_t i = 0; i < words.size(); i += options["wordsPerLine"]) {
            size_t end = std::min(i + options["wordsPerLine"], words.size());
            std::string line;
            for (size_t j = i; j < end; ++j) {
                line += words[j] + " ";
            }
            line.pop_back(); // Remove trailing space
            lines.push_back(line);
        }

        // Create pages from lines
        pages.clear();
        for (size_t i = 0; i < lines.size(); i += options["linesPerPage"]) {
            size_t end = std::min(i + options["linesPerPage"], lines.size());
            std::string page;
            for (size_t j = i; j < end; ++j) {
                page += lines[j] + "\n";
            }
            pages.push_back(page);
        }
    }

    int calculatePayment() {
        paidPages = words.size() / words.size();
        if (paidPages < 1) {
            return 0;
        } else if (options.find(std::to_string(paidPages)) != options.end()) {
            return options[std::to_string(paidPages)];
        } else {
            return options["default"];
        }
    }

    void displayPages() {
        int payment = calculatePayment();
        std::cout << "Total Pages: " << pages.size() << std::endl;
        std::cout << "Paid Pages: " << (paidPages > 0 ? paidPages : 0) << std::endl;
        std::cout << "Payment Due: $" << payment << std::endl;

        for (size_t i = 0; i < pages.size(); ++i) {
            std::cout << "\nPage " << (i + 1) << ":\n" << pages[i] << "\n";
        }
    }

    void processArticle() {
        splitIntoPages();
        displayPages();
    }
};

int main() {
    std::map<std::string, int> options = {
        {"wordsPerLine", 12},
        {"linesPerPage", 20},
        {"1", 30},
        {"2", 30},
        {"3", 60},
        {"4", 60},
        {"default", 100}
    };


    std::string articleText; 
    std::string line;
                                                                  //
    std::ifstream nameFilein;
    nameFilein.open("writing.txt");
    while ( getline(nameFilein, line) ) {
        articleText += line + " ";
    }
    nameFilein.close();

    ArticleManager articleManager(articleText, options);
    articleManager.processArticle();

    return 0;
}
