package Observer;

import java.util.ArrayList;
import java.util.List;

public class Order implements Observable {
    private String position;
    private String destination;
    private int timeBeforeArrival;
    private List<Observer> observers;

    public Order() {
        this.observers = new ArrayList<>();
    }

    public String getPosition() {
        return position;
    }

    public String getDestination() {
        return destination;
    }

    public int getTimeBeforeArrival() {
        return timeBeforeArrival;
    }

    public void setData(String position, String destination, int timeBeforeArrival) {
        this.position = position;
        this.destination = destination;
        this.timeBeforeArrival = timeBeforeArrival;
    }

    @Override
    public void addObserver(Observer observer) {
        observers.add(observer);
    }

    @Override
    public boolean notifyObservers() {
        if (observers != null) {
            for (Observer observer : observers) {
                observer.update(this);
            }
            return true;
        }
        return false;
    }
}
