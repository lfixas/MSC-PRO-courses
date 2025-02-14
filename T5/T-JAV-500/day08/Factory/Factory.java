package Factory;

import java.util.ArrayList;
import java.util.List;

public class Factory {

    public Toy create(String gift) throws NoSuchToyException {
        if (gift.equals("teddy")) {
            TeddyBear teddyBear = new TeddyBear();
            return (Toy) teddyBear;
        } else if (gift.equals("gameboy")) {
            Gameboy gameBoy = new Gameboy();
            return (Toy) gameBoy;
        } else {
            throw new NoSuchToyException("No such toy: " + gift + ".");
        }
    }

    public List<GiftPaper> getPapers(int n) {
        List<GiftPaper> giftPapers = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            giftPapers.add(new GiftPaper());
        }
        return giftPapers;
    }
}
