<template>
  <ValidationProvider :name="$attrs.label" :rules="rules" v-slot="{ errors, valid }">
    <v-text-field
		:readonly="readonly"
      v-model="innerValue"
      :error-messages="errors"
      :success="valid"
      v-bind="$attrs"
		:counter="counter"
      v-on="$listeners"
		dense
		solo
    ></v-text-field>
  </ValidationProvider>
</template>

<script>
import { ValidationProvider } from "vee-validate";

export default {
  name: 'ValidationTextfield',
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
	counter: {
		type: Number,
		default: 50		
	},
    // must be included in props
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

