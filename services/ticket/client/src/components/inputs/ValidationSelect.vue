<template>
  <ValidationProvider :name="$attrs.label" :rules="rules" v-slot="{ errors }">
    <v-select :readonly="readonly" v-model="innerValue" :error-messages="errors" v-bind="$attrs" v-on="$listeners" ense solo></v-select>
  </ValidationProvider>
</template>

<script>
import { ValidationProvider } from "vee-validate";

export default {
  name: 'ValidationSelect',
  components: {
    ValidationProvider
  },
  props: {
    rules: {
      type: [Object, String],
      default: ""
    },
	readonly:{
		type: Boolean,
		default: true
	},
    value: {
      type: null
    }
  },
  data: () => ({
    innerValue: ""
  }),
  watch: {
    // Handles internal model changes.
    innerValue(newVal) {
      this.$emit("input", newVal);
    },
    // Handles external model changes.
    value(newVal) {
      this.innerValue = newVal;
    }
  },
  created() {
    if (this.value) {
      this.innerValue = this.value;
    }
  }
};
</script>

