import { mount } from "@vue/test-utils";
import ContactForm from "../src/components/ContactForm.vue";


global.alert = vi.fn(); // Добавляет пустую заглушку для alert()



describe("ContactForm.vue", () => {
  it("рендерит корректно", () => {
    const wrapper = mount(ContactForm);
    expect(wrapper.find("h2").text()).toBe("Contact Us");
  });

  it("обновляет данные формы", async () => {
    const wrapper = mount(ContactForm);
    const nameInput = wrapper.find("input#name");
    const emailInput = wrapper.find("input#email");
    const messageInput = wrapper.find("textarea#message");

    await nameInput.setValue("John Doe");
    await emailInput.setValue("john@example.com");
    await messageInput.setValue("Hello!");

    expect(wrapper.vm.form.name).toBe("John Doe");
    expect(wrapper.vm.form.email).toBe("john@example.com");
    expect(wrapper.vm.form.message).toBe("Hello!");
  });

  it("отправляет данные и очищает форму", async () => {
    global.fetch = vi.fn(() =>
      Promise.resolve({
        json: () => Promise.resolve({ status: "success" }),
      })
    );

    const wrapper = mount(ContactForm);
    await wrapper.find("form").trigger("submit.prevent");

    expect(global.fetch).toHaveBeenCalledTimes(1);
    expect(wrapper.vm.form.name).toBe("");
    expect(wrapper.vm.form.email).toBe("");
    expect(wrapper.vm.form.message).toBe("");
  });
});
