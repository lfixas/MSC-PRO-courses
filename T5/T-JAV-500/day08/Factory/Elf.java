package Factory;

import java.util.ArrayList;
import java.util.List;

public class Elf {
    private Toy toy;
    private List<GiftPaper> papers;
    private Factory factory;

    public Elf(Factory factory) {
        this.factory = factory;
        this.papers = new ArrayList<>();
    }

    public boolean pickToy(String gift) {
        if (toy != null) {
            System.out.println("Minute please?! I'm not that fast.");
            return false;
        }

        try {
            toy = factory.create(gift);
            System.out.println("What a nice one! I would have liked to keep it...");
            return true;
        } catch (NoSuchToyException exception) {
            System.out.println("I didn't find any " + gift + ".");
            return false;
        }
    }

    public boolean pickPapers(int nb) {
        List<GiftPaper> newPapers = factory.getPapers(nb);
        if (newPapers != null) {
            papers.addAll(newPapers);
            return true;
        }
        return false;
    }

    public GiftPaper pack() {
        // if (toy == null && !papers.isEmpty()) {
        //     System.out.println("I don't have any toy, but hey at least it's paper!");
        //     return null;
        // }
        if (papers.isEmpty()) {
            System.out.println("Wait... I can't pack it with my shirt.");
            return null;
        }

        if (toy == null) {
            System.out.println("I don't have any toy, but hey at least it's paper!");
            papers.remove(0);
            return null;
        }        

        GiftPaper giftPaper = new GiftPaper();
        giftPaper.wrap(toy);
        toy = null;
        this.toy = null;
        papers.remove(0);
        System.out.println("And another kid will be happy!");
        return giftPaper;
    }
}
