import { expect } from "chai";

export const testAction = (
  store,
  action,
  actionPayload,
  state,
  expectedMutations,
  done
) => {
  console.log('mkhee')
	console.log(done)
  let count = 0;
  let commit = (type, payload) => {
    let mutation = expectedMutations[count];
    try {
		 console.log(type)
		 console.log(mutation.type)
      // check if commit function is invoked with expected args
      expect(mutation.type).to.equal(type);
      if (payload) {
        expect(mutation.payload).to.deep.equal(payload);
      }
      count++;
      // check if all mutations have been dispatched
      if (count >= expectedMutations.length) {
        done();
      }
    } catch (error) {
      done(error);
    }
  };

  if (expectedMutations.length === 0) {
    expect(count).to.equal(0);
    done();
  } else {
    store.dispatch(action,{commit, state}, actionPayload);
  }
};
