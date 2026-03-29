Come up with as many analogies as possible to explain what mocking is. See if you can come up with the most ridiculous analogy in the room.

	•	The Stunt Double Analogy: Mocking is like hiring a stunt double in a movie. The stunt double stands in for the actor during dangerous or complex scenes so that the main actor doesn’t have to. Similarly, a mock “stands in” for a real object during testing.

	•	The Substitute Teacher Analogy: Imagine a classroom where the regular teacher is out sick, and a substitute teacher comes in. The substitute has a rough idea of how the class runs, but they’re just there to maintain structure without the full expertise. In mocking, the “substitute” object temporarily replaces the actual class, helping you test interactions without the real thing.


Come up with different piece of software for every student at your table. For each piece of software, identify one way developers would have used mocking to test it. Make sure you use a different example for each piece of software.

E-commerce Website
Mocking example: When testing the checkout process, developers can mock the payment gateway to simulate various transaction outcomes (successful, failed, or pending) without interacting with a real bank or payment processor.


Come up with examples of when it would not be appropriate to use mocking, and why.

	•	Real-Time Systems: For systems that rely on real-time data and performance, such as a high-frequency trading platform, mocking might hide performance bottlenecks or concurrency issues. It’s important to test the system under real-world loads to ensure reliability.
    •	Security Testing: Mocking security components like authentication services or encryption systems can lead to overconfidence in their behavior. It’s critical to test security systems with real scenarios to identify vulnerabilities.


What are the risks of using mocking?

	•	False Sense of Security: Mocked dependencies may not behave exactly like the real thing. Tests could pass with mocks but fail in production if the real components behave differently (e.g., timing issues, data formats).
	•	Over-mocking: If you mock too many dependencies, your tests might not provide a useful reflection of the real system. This can lead to tests that are not meaningful because they do not resemble how the system will actually run.
