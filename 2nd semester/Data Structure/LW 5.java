import java.util.*;
public class Main    {
    public static void main(String[] args) {
        ArrayList<String[]> nameAges = new ArrayList<>();
        nameAges.add(new String[]{"Daniil", "17"});
        nameAges.add(new String[]{"Ivan", "18"});
        nameAges.add(new String[]{"Artem", "18"});
        nameAges.add(new String[]{"Anna", "19"});

        int minAge = Integer.parseInt(nameAges.get(0)[1]);
        int index = 0;

        for (int i = 1; i < nameAges.size(); i++) {
            int age = Integer.parseInt(nameAges.get(i)[1]);
            if (age < minAge) {
                minAge = age;
                index = i;
            }
        }

        System.out.println("The youngest person is " + nameAges.get(index)[0] + " who is " + minAge + " years old.");
    }
}
