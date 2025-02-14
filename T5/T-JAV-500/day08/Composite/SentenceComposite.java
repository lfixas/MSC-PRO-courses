package Composite;

import java.util.ArrayList;
import java.util.List;

public class SentenceComposite implements Sentence {
    private List<Sentence> childSentences;

    public SentenceComposite() {
        childSentences = new ArrayList<>();
    }

    @Override
    public void print() {
        for (Sentence sentence : childSentences) {
            sentence.print();
        }
    }

    public void add(Sentence sentence) {
        childSentences.add(sentence);
    }

    public void remove(Sentence sentence) {
        childSentences.remove(sentence);
    }
}
