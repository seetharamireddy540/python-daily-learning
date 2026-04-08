/**
 * Complete guide to division operations in Java (Python divmod equivalent)
 * 
 * Java doesn't have a built-in divmod function, but you can:
 * 1. Use / and % operators separately
 * 2. Create a custom divmod method
 * 3. Use Math.floorDiv() and Math.floorMod() for floor division
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class DivModTutorial {

    // ========================================================================
    // 1. CUSTOM DIVMOD CLASS
    // ========================================================================
    
    static class DivModResult {
        final int quotient;
        final int remainder;
        
        DivModResult(int quotient, int remainder) {
            this.quotient = quotient;
            this.remainder = remainder;
        }
        
        @Override
        public String toString() {
            return "(" + quotient + ", " + remainder + ")";
        }
    }
    
    static DivModResult divmod(int dividend, int divisor) {
        int quotient = dividend / divisor;
        int remainder = dividend % divisor;
        return new DivModResult(quotient, remainder);
    }
    
    static class DivModResultLong {
        final long quotient;
        final long remainder;
        
        DivModResultLong(long quotient, long remainder) {
            this.quotient = quotient;
            this.remainder = remainder;
        }
        
        @Override
        public String toString() {
            return "(" + quotient + ", " + remainder + ")";
        }
    }
    
    static DivModResultLong divmod(long dividend, long divisor) {
        long quotient = dividend / divisor;
        long remainder = dividend % divisor;
        return new DivModResultLong(quotient, remainder);
    }

    // ========================================================================
    // 2. DIVISION OPERATORS IN JAVA
    // ========================================================================
    
    static void divisionOperators() {
        System.out.println("JAVA DIVISION OPERATORS");
        System.out.println("=======================\n");
        
        int a = 17, b = 5;
        System.out.println("a = " + a + ", b = " + b + "\n");
        
        // Regular division (truncates toward zero for integers)
        System.out.println("a / b  = " + (a / b));           // 3 (integer division)
        System.out.println("(double)a / b = " + ((double)a / b)); // 3.4 (float division)
        
        // Modulo (remainder)
        System.out.println("a % b  = " + (a % b));           // 2
        
        // Custom divmod
        DivModResult result = divmod(a, b);
        System.out.println("divmod(a, b) = " + result);      // (3, 2)
        
        // Verify
        System.out.println("\nVerify: " + result.quotient + " * " + b + " + " + 
                          result.remainder + " = " + (result.quotient * b + result.remainder));
    }

    // ========================================================================
    // 3. PRACTICAL USE CASES
    // ========================================================================
    
    static String convertSecondsToTime(int totalSeconds) {
        DivModResult hm = divmod(totalSeconds, 3600);
        int hours = hm.quotient;
        
        DivModResult ms = divmod(hm.remainder, 60);
        int minutes = ms.quotient;
        int seconds = ms.remainder;
        
        return hours + "h " + minutes + "m " + seconds + "s";
    }
    
    static String convertCentsToDollars(int cents) {
        DivModResult result = divmod(cents, 100);
        return String.format("$%d.%02d", result.quotient, result.remainder);
    }
    
    static String splitIntoGroups(int totalItems, int groupSize) {
        DivModResult result = divmod(totalItems, groupSize);
        return result.quotient + " groups of " + groupSize + ", " + 
               result.remainder + " left over";
    }

    // ========================================================================
    // 4. NEGATIVE NUMBERS - KEY DIFFERENCE!
    // ========================================================================
    
    static void negativeNumbers() {
        System.out.println("NEGATIVE NUMBERS - JAVA vs PYTHON");
        System.out.println("===================================\n");
        
        System.out.println("Java / and % truncate toward ZERO");
        System.out.println("Python // and % floor toward NEGATIVE INFINITY\n");
        
        // Java behavior
        System.out.println("JAVA:");
        System.out.println("17 / 5   = " + (17 / 5));      // 3
        System.out.println("-17 / 5  = " + (-17 / 5));     // -3 (truncates toward zero)
        System.out.println("17 % 5   = " + (17 % 5));      // 2
        System.out.println("-17 % 5  = " + (-17 % 5));     // -2 (sign matches dividend)
        
        // Python-like behavior using Math.floorDiv and Math.floorMod
        System.out.println("\nJAVA (Python-like with Math.floorDiv/floorMod):");
        System.out.println("Math.floorDiv(17, 5)  = " + Math.floorDiv(17, 5));    // 3
        System.out.println("Math.floorDiv(-17, 5) = " + Math.floorDiv(-17, 5));   // -4 (floors down)
        System.out.println("Math.floorMod(17, 5)  = " + Math.floorMod(17, 5));    // 2
        System.out.println("Math.floorMod(-17, 5) = " + Math.floorMod(-17, 5));   // 3 (always positive)
    }

    // ========================================================================
    // 5. REAL-WORLD EXAMPLES
    // ========================================================================
    
    static String formatBytes(long bytesCount) {
        long gb = 1024L * 1024 * 1024;
        long mb = 1024L * 1024;
        long kb = 1024L;
        
        DivModResultLong r1 = divmod(bytesCount, gb);
        DivModResultLong r2 = divmod(r1.remainder, mb);
        DivModResultLong r3 = divmod(r2.remainder, kb);
        
        List<String> parts = new ArrayList<>();
        if (r1.quotient > 0) parts.add(r1.quotient + "GB");
        if (r2.quotient > 0) parts.add(r2.quotient + "MB");
        if (r3.quotient > 0) parts.add(r3.quotient + "KB");
        if (r3.remainder > 0) parts.add(r3.remainder + "B");
        
        return parts.isEmpty() ? "0B" : String.join(" ", parts);
    }
    
    static int paginate(int totalItems, int itemsPerPage) {
        DivModResult result = divmod(totalItems, itemsPerPage);
        int totalPages = result.quotient;
        if (result.remainder > 0) {
            totalPages++;
        }
        return totalPages;
    }
    
    static String decimalToBase(int number, int base) {
        if (number == 0) return "0";
        
        String digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        List<Character> result = new ArrayList<>();
        
        while (number > 0) {
            DivModResult dm = divmod(number, base);
            number = dm.quotient;
            result.add(digits.charAt(dm.remainder));
        }
        
        Collections.reverse(result);
        StringBuilder sb = new StringBuilder();
        for (char c : result) sb.append(c);
        return sb.toString();
    }

    // ========================================================================
    // 6. PERFORMANCE COMPARISON
    // ========================================================================
    
    static void performanceTest() {
        int iterations = 10_000_000;
        int a = 123456789, b = 7;
        
        // Using separate operations
        long start1 = System.nanoTime();
        for (int i = 0; i < iterations; i++) {
            int q = a / b;
            int r = a % b;
        }
        long time1 = System.nanoTime() - start1;
        
        // Using divmod method
        long start2 = System.nanoTime();
        for (int i = 0; i < iterations; i++) {
            DivModResult result = divmod(a, b);
        }
        long time2 = System.nanoTime() - start2;
        
        System.out.println("Separate / and %: " + time1 / 1_000_000 + "ms");
        System.out.println("divmod method:    " + time2 / 1_000_000 + "ms");
        System.out.println("\nNote: In Java, separate operations are usually faster");
        System.out.println("because the JVM optimizes them. Use divmod for clarity.");
    }

    // ========================================================================
    // MAIN DEMO
    // ========================================================================
    
    public static void main(String[] args) {
        System.out.println("=".repeat(60));
        System.out.println("1. DIVISION OPERATORS");
        System.out.println("=".repeat(60));
        divisionOperators();
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("2. PRACTICAL EXAMPLES");
        System.out.println("=".repeat(60));
        System.out.println(convertSecondsToTime(3665));
        System.out.println(convertCentsToDollars(1234));
        System.out.println(splitIntoGroups(47, 5));
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("3. NEGATIVE NUMBERS");
        System.out.println("=".repeat(60));
        negativeNumbers();
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("4. REAL-WORLD EXAMPLES");
        System.out.println("=".repeat(60));
        System.out.println("Bytes: " + formatBytes(5_368_709_120L));
        System.out.println("Pages needed for 100 items (10/page): " + paginate(100, 10));
        System.out.println("255 in binary: " + decimalToBase(255, 2));
        System.out.println("255 in hex: " + decimalToBase(255, 16));
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("5. PERFORMANCE");
        System.out.println("=".repeat(60));
        performanceTest();
    }
}
